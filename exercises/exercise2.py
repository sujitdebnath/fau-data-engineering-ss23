# Python imports
import os, sys
import sqlite3
import urllib.request, urllib.error
from typing import List, Dict

# Third party imports
import pandas as pd


class DataPipeline:
    """
    A class to represent an ETL pipeline.

    Attributes:
        source_info (dict): A dictionary represents the information of data source.
        db_config (dict): A dictionary represents the output DB name and corresponding table name.
    
    Methods:
        on_extract(source_info: Dict) ->  str: Extracts data from the source.
        on_transform(extracted_data: str) -> pd.DataFrame: Transforms the input data by applying necessary transformations.
        on_load(transformed_data: pd.DataFrame) -> None: Loads transformed data into database.
        run_pipeline() -> None: Run the whole ETL pipeline.

        _download_data(url: str, output_path: str) -> None: Downloads data from the specified URL and saves it to the output path.
        _read_data(file_path: str, sep: str, compression: str, encoding: str) -> pd.DataFrame: Reads a file into a pandas DataFrame.
        _delete_file(file_path: str) -> None: Delete a file from the directory.
    """

    def __init__(self, source_info: Dict, db_config: Dict) -> None:
        self.source_info = source_info
        self.db_config = db_config
    
    def on_extract(self, source_info: Dict) ->  str:
        """
        Extracts data from the source.

        Parameters:
            source_info (dict): A dictionary represents the information of data source.

        Returns:
            extracted_data_path (str): A string containing the path of extracted csv data.
        """
        extracted_data_path = os.path.join(os.getcwd(), source_info['file_name'])
        self._download_data(source_info['url'], extracted_data_path)

        return extracted_data_path

    def on_transform(self, extracted_data: str) -> pd.DataFrame:
        """
        Transforms the input data by applying necessary transformations.

        Parameters:
            extracted_data (str): A string containing the path of extracted csv data.

        Returns:
            transformed_data (pd.DataFrame): A pandas DataFrame that contains transformed data.
        """
        transformed_data = self._read_data(file_path=extracted_data, sep=';', encoding='utf-8-sig')

        # perform necessary transformations - start
        print(f"Info: Necessary transformations is started")
        transformed_data = transformed_data.drop('Status', axis=1)
        transformed_data = transformed_data[transformed_data['Verkehr'].isin(['FV', 'RV', 'nur DPN'])]

        for col in ['Laenge', 'Breite']:
            transformed_data[col] = transformed_data[col].str.replace(',', '.').astype(float)
            transformed_data = transformed_data[(transformed_data[col] >= -90) & (transformed_data[col] <= 90)]
        
        # <exactly two characters>:<any amount of numbers>:<any amount of numbers><optionally another colon followed by any amount of numbers>
        pattern = r'^[A-Za-z]{2}:\d+:\d+(?::\d+)?$'
        transformed_data = transformed_data[transformed_data['IFOPT'].str.contains(pattern, regex=True, na=False)]

        transformed_data.dropna(inplace=True)
        transformed_data['Betreiber_Nr'] = transformed_data['EVA_NR'].astype(int)
        print(f"Succeed: Necessary transformations is successfully ended")
        # perform necessary transformations - end

        self._delete_file(extracted_data)

        return transformed_data

    def on_load(self, transformed_data: pd.DataFrame) -> None:
        """
        Loads transformed data into database.

        Parameters:
            transformed_data (pd.DataFrame): A pandas DataFrame that contains transformed data.
        
        Returns:
            None
        """
        try:
            # connect to the database
            conn = sqlite3.connect(self.db_config['db_name'])
            print(f"Succeed: Database created successfully")

            # insert data into the database
            transformed_data.to_sql(self.db_config['table_name'], conn, if_exists='replace', index=False)
            print(f"Succeed: Data inserted into the database successfully")
            
            # close the connection
            conn.close()
        except sqlite3.Error as e:
            print(f"Error: An error occurred during table population: {str(e)}")
            sys.exit(1)

    def run_pipeline(self) -> None:
        """
        Run the whole ETL pipeline.

        Parameters:
            None

        Returns:
            None
        """
        # extract data from the source
        print("\n{} {} {}".format(20*"-", "Extract: data extraction from the source initiated", 20*"-"))
        extracted_data = self.on_extract(self.source_info)
        print("{} {} {}\n".format(20*"-", "Extract: data extraction from the source ended", 20*"-"))
        
        # transform the extracted data
        print("\n{} {} {}".format(20*"-", "Transform: data transformation from extracted data initiated", 20*"-"))
        transformed_data = self.on_transform(extracted_data)
        print("{} {} {}\n".format(20*"-", "Transform: data transformation from extracted data ended", 20*"-"))
        
        # load transformed data into database
        print("\n{} {} {}".format(20*"-", "Load: transformed data loading into a database initiated", 20*"-"))
        self.on_load(transformed_data)
        print("{} {} {}\n".format(20*"-", "Load: transformed data loading into a database ended", 20*"-"))
    
    def _download_data(self, url: str, output_path: str) -> None:
        """
        Downloads data from the specified URL and saves it to the output path.

        Parameters:
            url (str): The URL from which to download the data.
            output_path (str): The path where the downloaded data will be saved.
        
        Returns:
            None
        """
        try:
            urllib.request.urlretrieve(url, output_path)
            print(f"Succeed: Data downloaded successfully and saved as {output_path.split(os.sep)[-1]}")
        except urllib.error.URLError as e:
            print(f"Error: Failed to download data from URL. {str(e)}")
            sys.exit(1)
        except Exception as e:
            print(f"Error: An unexpected error occurred. {str(e)}")
            sys.exit(1)

    def _read_data(self, file_path: str, sep: str = ",",
                   header: int = 0,
                   names: List = None,
                   compression: str = None,
                   encoding: str = 'utf-8') -> pd.DataFrame:
        """
        Reads a file into a pandas DataFrame.

        Parameters:
            file_path (str): The path to the desired file.
            sep (str, optional): The seperator for the desired file.
            header (int, optional): Row number(s) to use as the column names, and the start of the data.
            names (list, optional): List of column names to use.
            compression (str, optional): The type of compression used on the file (e.g., 'gzip', 'zip').
            encoding (str, optional): The encoding of the desired file. Defaults to 'utf-8'.

        Returns:
            data_df (pd.DataFrame): The contents of the file as a pandas DataFrame.
        """
        try:
            data_df = pd.read_csv(file_path, sep=sep,
                                  header=header, names=names,
                                  compression=compression, encoding=encoding)
            print(f"Succeed: '{file_path.split(os.sep)[-1]}' is successfully loaded")
            return data_df
        except FileNotFoundError:
            print(f"Error: File not found- '{file_path}'")
            sys.exit(1)
        except Exception as e:
            print(f"Error: Failed reading the file- {str(e)}")
            sys.exit(1)
    
    def _delete_file(self, file_path: str) -> None:
        """
        Delete a file from the directory.

        Parameters:
            file_path (str): The desired file path.

        Returns:
            None
        """
        try:
            os.remove(file_path)
            print(f"Succeed: File '{file_path.split(os.sep)[-1]}' deleted successfully")
        except OSError as e:
            print(f"Error: Issue occurred while deleting the file: {str(e)}")
            sys.exit(1)
        except Exception as e:
            print(f"Error: Failed deleting the file- {str(e)}")
            sys.exit(1)


if __name__ == "__main__":
    source_data_info = {
        'file_name': "trainstops.csv",
        'url': "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
    }
    output_db_config = {'db_name': "trainstops.sqlite", 'table_name': "trainstops"}

    etl_pipeline = DataPipeline(source_data_info, output_db_config)
    etl_pipeline.run_pipeline()

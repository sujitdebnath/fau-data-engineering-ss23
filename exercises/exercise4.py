# Python imports
import os, sys
import shutil
import sqlite3
import zipfile
import urllib.request, urllib.error
from typing import List, Dict, Any

# Third party imports
import pandas as pd


class DataPipeline:

    def __init__(self, source_info: Dict, db_config: Dict) -> None:
        self.source_info = source_info
        self.db_config = db_config
    
    def on_extract(self, source_info: Dict) ->  str:
        # download the zip file
        zip_file_path = os.path.join(os.getcwd(), source_info['zip_file_name'])
        self._download_data(source_info['url'], zip_file_path)

        # extract the zip file
        zip_extract_path = os.path.join(os.getcwd(), source_info['zip_file_name'].split(".")[0])
        self._unzip_file(zip_file_path, zip_extract_path)

        # delete the zip file
        self._delete_file(zip_file_path)

        # move the data.csv to ./exercises
        data_file_path = os.path.join(zip_extract_path, source_info['data_file_name'])
        extracted_data_path = os.path.join(os.getcwd(), source_info['data_file_name'])
        os.replace(data_file_path, extracted_data_path)

        # remove the extracted zip file directory
        self._remove_directory(zip_extract_path)

        return extracted_data_path

    def on_transform(self, extracted_data: str) -> pd.DataFrame:
        columns = ["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]

        # read the extracted csv data as a pandas dataframe
        transformed_data = self._read_data(file_path=extracted_data, sep=';', decimal=',', usecols=columns, index_col=False)

        # rename columns
        transformed_data = transformed_data.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"})

        # transform temperatures in Celsius to Fahrenheit
        transformed_data[["Temperatur", "Batterietemperatur"]] = transformed_data[["Temperatur", "Batterietemperatur"]].apply(lambda x: round((x * 9/5) + 32, 2))

        # data validation - Geraet and Monat
        transformed_data = transformed_data[(transformed_data["Geraet"] > 0) & (transformed_data["Monat"] > 0)]

        # delete the extracted csv data
        self._delete_file(extracted_data)

        return transformed_data

    def on_load(self, transformed_data: pd.DataFrame) -> None:
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
        try:
            urllib.request.urlretrieve(url, output_path)
            print(f"Succeed: Data downloaded successfully and saved as {output_path.split(os.sep)[-1]}")
        except urllib.error.URLError as e:
            print(f"Error: Failed to download data from URL. {str(e)}")
            sys.exit(1)
        except Exception as e:
            print(f"Error: An unexpected error occurred. {str(e)}")
            sys.exit(1)

    def _unzip_file(self, zip_path: str, extract_path: str) -> None:
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            print("Succeed: File successfully extracted")
        except zipfile.BadZipFile:
            print("Error: Invalid zip file")
            sys.exit(1)
        except FileNotFoundError:
            print("Error: File or directory not found")
            sys.exit(1)
        except Exception as e:
            print(f"Error: An error occurred- {str(e)}")
            sys.exit(1)
    
    def _read_data(self, file_path: str, sep: str = ",",
                   header: int = 0,
                   names: List = None,
                   compression: str = None,
                   decimal: str = '.',
                   usecols: List = None,
                   index_col: Any = None,
                   encoding: str = 'utf-8') -> pd.DataFrame:
        try:
            data_df = pd.read_csv(file_path, sep=sep, header=header,
                                  names=names, decimal=decimal, usecols=usecols,
                                  index_col=index_col, compression=compression, encoding=encoding)
            print(f"Succeed: '{file_path.split(os.sep)[-1]}' is successfully loaded")
            return data_df
        except FileNotFoundError:
            print(f"Error: File not found- '{file_path}'")
            sys.exit(1)
        except Exception as e:
            print(f"Error: Failed reading the file- {str(e)}")
            sys.exit(1)
    
    def _delete_file(self, file_path: str) -> None:
        try:
            os.remove(file_path)
            print(f"Succeed: File '{file_path.split(os.sep)[-1]}' deleted successfully")
        except OSError as e:
            print(f"Error: Issue occurred while deleting the file: {str(e)}")
            sys.exit(1)
        except Exception as e:
            print(f"Error: Failed deleting the file- {str(e)}")
            sys.exit(1)
    
    def _remove_directory(self, directory_path: str):
        try:
            shutil.rmtree(directory_path)
            print(f"Succeed: {directory_path} directory successfully removed")
        except FileNotFoundError:
            print("Error: Directory not found")
        except PermissionError:
            print("Error: Permission denied")
        except Exception as e:
            print(f"Error: An error occurred- {str(e)}")


if __name__ == "__main__":
    source_data_info = {
        'zip_file_name': "mowesta-dataset-20221107.zip",
        'url': "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip",
        'data_file_name': "data.csv"
    }
    output_db_config = {'db_name': "temperatures.sqlite", 'table_name': "temperatures"}

    etl_pipeline = DataPipeline(source_data_info, output_db_config)
    etl_pipeline.run_pipeline()

# Python imports
import sys, calendar

# Third party imports
import pandas as pd

# Self imports


class DataTransformer:
    """
    A class to represent the data transformer of an ETL pipeline.

    Attributes:
        extracted_data (dict): A dictionary containing information of extracted data
        transformed_data (pd.DataFrame): A panda dataframe of transformed data.
    
    Methods:
        transform() -> None: Transforms the extracted data by applying necessary transformations.
        _read_data(file_path: str, sep: str, compression: str, encoding: str) -> pd.DataFrame:
            Reads a file into a pandas DataFrame.
    """

    def __init__(self) -> None:
        self.extracted_data = None
        self.transformed_data = pd.DataFrame()

    def transform(self) -> None:
        """
        Transforms the extracted data by applying necessary transformations.

        Parameters:
            None

        Returns:
            None
        """

        for source, files_list in self.extracted_data.items():
            # read and transformed data of source 1: Mobilithek
            if source == "Mobilithek":
                for year, file_name in files_list:
                    if int(year) >= 2016 and int(year)<=2022:
                        if int(year) >= 2016 and int(year)<=2020:
                            data_df = self._read_data(file_path=file_name, sep=';', encoding='utf-8-sig')
                        else:
                            data_df = self._read_data(file_path=file_name, sep=';', encoding='unicode_escape')
                        
                        data_df.rename(columns={data_df.columns[0]: 'Date'}, inplace=True)
                        data_df.fillna(0, inplace=True)
                        data_df['Date'] = data_df['Date'].replace(
                            data_df['Date'].unique(),
                            [month+"-"+year for month in calendar.month_name[1:]])
                        data_df[data_df.columns[1:]] = data_df[data_df.columns[1:]] * 1000
                        data_df = data_df.astype({col:'int64' for col in data_df.columns[1:]})
                    else:
                        data_df = self._read_data(file_path=file_name, sep=';', encoding='unicode_escape')

                        data_df.rename(columns={data_df.columns[0]: 'Date'}, inplace=True)
                        data_df.drop(data_df[data_df['Date'] == 'Jahressumme'].index, inplace=True)
                        data_df.fillna(0, inplace=True)
                        data_df = data_df.astype({col:'int64' for col in data_df.columns[1:]})
                        data_df['Date'] = data_df['Date'].replace(
                            data_df['Date'].unique(),
                            [month+"-"+year for month in calendar.month_name[1:]])
                    
                    print(f"Succeed: Transformation of {file_name} to dataframe is successfully done")
                    print(data_df)
            
            # read and transformed data of source 2: Meteostat
            elif source == "Meteostat":
                print("Meteostat")

    def _read_data(self, file_path: str, sep: str = None,
                   compression: str = None, encoding: str = 'utf-8') -> pd.DataFrame:
        """
        Reads a file into a pandas DataFrame.

        Parameters:
            file_path (str): The path to the desired file.
            sep (str, optional): The seperator for the desired file.
            compression (str, optional): The type of compression used on the file (e.g., 'gzip', 'zip').
            encoding (str, optional): The encoding of the desired file. Defaults to 'utf-8'.

        Returns:
            data_df (pd.DataFrame): The contents of the file as a pandas DataFrame.
        """
        try:
            data_df = pd.read_csv(file_path, sep=sep, compression=compression, encoding=encoding)
            print(f"Succeed: {file_path} is successfully loaded")
            return data_df
        except FileNotFoundError:
            print(f"Error: File not found- {file_path}")
            sys.exit(1)
        except Exception as e:
            print(f"Error: Failed reading the file- {str(e)}")
            sys.exit(1)

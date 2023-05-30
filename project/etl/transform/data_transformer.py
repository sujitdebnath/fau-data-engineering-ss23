# Python imports
from typing import List
import os, sys, calendar

# Third party imports
import pandas as pd

# Self imports
from config.config_var import *


class DataTransformer:
    """
    A class to represent the data transformer of an ETL pipeline.

    Attributes:
        extracted_data (dict): A dictionary containing information of extracted data
        transformed_data (dict): A dict that contains transformed data.
    
    Methods:
        transform() -> None: Transforms the extracted data by applying necessary transformations.
        _read_data(file_path: str, sep: str, compression: str, encoding: str) -> pd.DataFrame:
            Reads a file into a pandas DataFrame.
        _delete_file(file_path: str) -> None: Delete a file from the directory.
    """

    def __init__(self) -> None:
        self.extracted_data = None
        self.transformed_data = dict()

    def transform(self) -> None:
        """
        Transforms the extracted data by applying necessary transformations.

        Parameters:
            None

        Returns:
            None
        """
        for source, files_list in self.extracted_data.items():
            # read, transformed and merge data of source 1: Mobilithek
            if source == "Mobilithek":
                temp_df_list = []

                # read and transformed data of source 1: Mobilithek
                for year, file_name in files_list:
                    file_path = os.path.join(DOWNLOADED_RAW_FILE_PATH, file_name)

                    if int(year) >= 2016 and int(year)<=2022:
                        if int(year) >= 2016 and int(year)<=2020:
                            data_df = self._read_data(file_path=file_path, sep=';', encoding='utf-8-sig')
                        else:
                            data_df = self._read_data(file_path=file_path, sep=';', encoding='unicode_escape')
                        
                        data_df.rename(columns={data_df.columns[0]: 'Date'}, inplace=True)
                        data_df.fillna(0, inplace=True)
                        data_df['Date'] = data_df['Date'].replace(
                            data_df['Date'].unique(),
                            [month+"-"+year for month in calendar.month_name[1:]])
                        data_df[data_df.columns[1:]] = data_df[data_df.columns[1:]] * 1000
                        data_df = data_df.astype({col:'int64' for col in data_df.columns[1:]})
                    else:
                        data_df = self._read_data(file_path=file_path, sep=';', encoding='unicode_escape')

                        data_df.rename(columns={data_df.columns[0]: 'Date'}, inplace=True)
                        data_df.drop(data_df[data_df['Date'] == 'Jahressumme'].index, inplace=True)
                        data_df.fillna(0, inplace=True)
                        data_df = data_df.astype({col:'int64' for col in data_df.columns[1:]})
                        data_df['Date'] = data_df['Date'].replace(
                            data_df['Date'].unique(),
                            [month+"-"+year for month in calendar.month_name[1:]])
                    
                    print(f"Succeed: Transformation of {file_name} to dataframe is successfully done")
                    temp_df_list.append(data_df)
                    self._delete_file(file_path)
                
                # merge data of source 1: Mobilithek
                merged_df = pd.concat([data_df for data_df in temp_df_list], axis=0, ignore_index=True)
                merged_df.fillna(0, inplace=True)
                merged_df = merged_df.astype({col:'int64' for col in merged_df.columns[1:]})
                # merged_df.to_csv(source+'.csv', index=False, encoding='utf-8-sig')
                print(f"Succeed: Extracted data from {source} are successfully transformed and merged")
            
            # read, transformed and merge data of source 2: Meteostat
            elif source == "Meteostat":
                temp_df_list = []
                parameters = ["year", "month", "tavg", "tmin", "tmax", "prcp", "wspd", "pres", "tsun"]

                # read and transformed data of source 2: Meteostat
                for station_id, _, file_name in files_list:
                    file_path = os.path.join(DOWNLOADED_RAW_FILE_PATH, file_name)
                    data_df = self._read_data(file_path=file_path, header=None, names=parameters, compression='gzip')
                    
                    data_df = data_df.loc[(data_df['year'] >= 2009) & (data_df['year'] <= 2022)]
                    data_df['month'] = data_df['month'].replace(
                            [num for num in range(1, 13)],
                            [month for month in calendar.month_name[1:]])
                    data_df['date'] = data_df['month'] + "-" + data_df['year'].astype(str)
                    data_df.drop(['month', 'year'], inplace=True, axis=1)
                    data_df = data_df[['date'] + [col for col in data_df.columns if col != 'date']]
                    data_df.rename(columns={col:col+"_"+station_id for col in data_df.columns if col != 'date'}, inplace=True)
                    data_df.fillna(0, inplace=True)
                    data_df = data_df.reset_index(drop=True)

                    print(f"Succeed: Transformation of {file_name} to dataframe is successfully done")
                    temp_df_list.append(data_df)
                    self._delete_file(file_path)
                
                # merge data of source 2: Meteostat
                merged_df = pd.merge(temp_df_list[0], temp_df_list[1], on='date', how='outer')
                merged_df.fillna(0, inplace=True)
                # merged_df.to_csv(source+'.csv', index=False)
                print(f"Succeed: Extracted data from {source} are successfully transformed and merged")
            
            self.transformed_data[source] = merged_df

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
            header (int, optional): 
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
            print(f"Succeed: File '{file_path.split(os.sep)[-1]}' deleted successfully.")
        except OSError as e:
            print(f"Error: Issue occurred while deleting the file: {str(e)}")
            sys.exit(1)
        except Exception as e:
            print(f"Error: Failed deleting the file- {str(e)}")
            sys.exit(1)

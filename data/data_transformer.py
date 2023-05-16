# Python imports
import sys

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
        pass

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
            DataFrame: The contents of the file as a pandas DataFrame.
        """
        try:
            return pd.read_csv(file_path, sep=sep, compression=compression, encoding=encoding)
        except FileNotFoundError:
            print(f"Error: File not found- {file_path}")
            sys.exit(1)
        except Exception as e:
            print(f"Error: Failed reading the file- {str(e)}")
            sys.exit(1)

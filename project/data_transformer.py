# Python imports

# Third party imports
import pandas as pd

# Self imports


class DataTransformer:
    """
    A class to represent the data transformer of an ETL pipeline.

    Attributes:
        extracted_data (list): A list of strings which represent the raw data file path of extracted data.
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

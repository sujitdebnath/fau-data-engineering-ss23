"""
Script Name: data_pipeline.py
Script Description: This script implements ETL pipeline for collecting and processing data from multiple sources
Author: Sujit Debnath
Author Email: sujit.debnath.bd@gmail.com
University: Friedrich-Alexander University Erlangen-Nuremberg
Course: Data Engineering (AMSE/SAKI)
Semester: SS2023
"""

# Python imports
from typing import List, Dict

# Third party imports
import pandas as pd

# Self imports


class PipelineService:
    """
    A class for providing external services to the DataPipeline class

    Attributes:
        None

    Methods:
        None
    """

    def __init__(self) -> None:
        pass


class DataPipeline:
    """
    A class to represent an ETL pipeline.

    Attributes:
        pipeline_service (PipelineService, optional): An object of PipelineService class for accessing external helps other than ETL

    Methods:
        extract(source_info: Dict) ->  List: Extracts data from multiple sources.
        transform(extracted_data: pd.DataFrame) -> pd.DataFrame: Transforms the input data by applying necessary transformations.
        load(transformed_data: pd.DataFrame) -> None: Loads transformed data into database.
    """

    def __init__(self, pipeline_service: PipelineService = PipelineService()) -> None:
        """
        Constructs all the necessary attributes for the DataPipeline object.

        Parameters:
            pipeline_service (PipelineService, optional): An object of PipelineService class for accessing external helps other than ETL
        
        Returns:
            None
        """
        self.pipeline_service = pipeline_service
    
    def extract(self, source_info: Dict) ->  List:
        """
        Extracts data from multiple sources.

        Parameters:
        source_info (Dict): A dictionary containing the necessary source URL and other information

        Returns:
            extracted_data_list (List): A list of panda dataframe of extracted data
        """

        return None

    def transform(self, extracted_data: pd.DataFrame) -> pd.DataFrame:
        """
        Transforms the input data by applying necessary transformations.

        Parameters:
            extracted_data (pd.DataFrame): A panda dataframe of all the extracted data.

        Returns:
            transformed_data (pd.DataFrame): A panda dataframe of transformed data.
        """

        return None

    def load(self, transformed_data: pd.DataFrame) -> None:
        """
        Loads transformed data into database.

        Parameters:
            transformed_data (pd.DataFrame): A panda dataframe of transformed data.
        
        Returns:
            None
        """

        pass


if __name__ == '__main__':
    source_info = dict()

    # extract data from multiple sources

    # combine data from both sources

    # transform data

    # load transformed data into database
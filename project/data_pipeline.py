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
from typing import List, Dict, Union
import sys, os

# Third party imports
import pandas as pd

# Self imports
from service_factory import HelperService
from data_extractor import DataExtractor
from data_transformer import DataTransformer
from data_loader import DataLoader


class DataPipeline:
    """
    A class to represent an ETL pipeline.

    Attributes:
        extractor (DataExtractor): An object of DataExtractor class for extracting data
        transformer (DataTransformer): An object of DataTransformer class for transforming data
        loader (DataLoader): An object of DataLoader class for loading data

    Methods:
        extract(source_info: Dict) ->  List: Extracts data from multiple sources.
        transform(extracted_data: pd.DataFrame) -> pd.DataFrame: Transforms the input data by applying necessary transformations.
        load(transformed_data: pd.DataFrame) -> None: Loads transformed data into database.
        run_pipeline() -> None: Run the whole ETL pipeline.
    """

    def __init__(
            self,
            helper_service: HelperService,
            extractor: DataExtractor,
            transformer: DataTransformer,
            loader: DataLoader
            ) -> None:
        self.helper_service = helper_service
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader
    
    def on_extract(self, source_info: Dict) ->  List:
        """
        Extracts data from multiple sources.

        Parameters:
            None

        Returns:
            extracted_data_list (list): A list of panda dataframe of extracted data
        """
        return None

    def on_transform(self, extracted_data: List) -> pd.DataFrame:
        """
        Transforms the input data by applying necessary transformations.

        Parameters:
            extracted_data (pd.DataFrame): A panda dataframe of all the extracted data.

        Returns:
            transformed_data (pd.DataFrame): A panda dataframe of transformed data.
        """

        return None

    def on_load(self, transformed_data: pd.DataFrame) -> None:
        """
        Loads transformed data into database.

        Parameters:
            transformed_data (pd.DataFrame): A panda dataframe of transformed data.
        
        Returns:
            None
        """

        pass

    def run_pipeline(self) -> None:
        """
        Run the whole ETL pipeline.

        Parameters:
            None

        Returns:
            None
        """
        source_info = helper_service.load_json("source_info.json")
        if not source_info:
            sys.exit(1)
        
        extracted_data = self.on_extract(source_info) # extract data from multiple sources
        transformed_data = self.on_transform(extracted_data) # combine and transform data from both sources
        loaded_data = self.on_load(transformed_data) # load transformed data into database


if __name__ == '__main__':
    helper_service = HelperService() # create a object of HelperService
    data_extractor = DataExtractor() # create a object of DataExtractor
    data_transformer = DataTransformer() # create a object of DataTransformer
    data_loader = DataLoader() # create a object of DataLoader

    # create a object of DataPipeline using helper service, extractor, transformer and loader object
    etl_data_pipeline = DataPipeline(
        helper_service = helper_service,
        extractor = data_extractor,
        transformer = data_transformer,
        loader = data_loader
    )

    # etl_data_pipeline.run_pipeline() # run the ETL pipeline
    
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
import json, sys, requests, os

# Third party imports
import pandas as pd

# Self imports


class PipelineServiceError(Exception):
    """
    An exception class for raising errors when error occurs in PipelineService class

    Attributes:
        None

    Methods:
        None
    """
    pass


class PipelineService:
    """
    A class for providing external services to the DataPipeline class

    Attributes:
        None

    Methods:
        load_json(file_path: str) -> Dict: Loads a JSON file as a dictionary.
        download_data(url: str, output_path: str) -> None: Downloads data from the specified URL and saves it to the output path.
    """

    def __init__(self) -> None:
        pass

    def load_json(self, file_path: str) -> Dict:
        """
        Loads a JSON file as a dictionary.

        Parameters:
            file_path (str): Path to the JSON file.

        Returns:
            data (dict): Loaded JSON data as a dictionary.
        
        Raises:
            PipelineServiceError: If loading of JSON file fails or encounters an error.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            raise PipelineServiceError(f"Error: File '{file_path}' not found.")
        except json.JSONDecodeError:
            raise PipelineServiceError(f"Error: Failed to decode JSON data in file '{file_path}'.")
        except Exception as e:
            raise PipelineServiceError(f"Error: An unexpected error occurred. {str(e)}")

    def download_data(self, url: str, output_path: str) -> None:
        """
        Downloads data from the specified URL and saves it to the output path.

        Parameters:
            url (str): The URL from which to download the data.
            output_path (str): The path where the downloaded data will be saved.

        Raises:
            PipelineServiceError: If the download fails or encounters an error.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an exception if the request was unsuccessful

            with open(output_path, 'wb') as file:
                file.write(response.content)

            print(f"Succeed: Data downloaded successfully and saved to: {output_path}")
        except requests.exceptions.ConnectionError as e:
            raise PipelineServiceError(f"Error: Failed to download data from URL due to Connection error.")
        except requests.exceptions.HTTPError as e:
            raise PipelineServiceError(f"Error: Failed to download data from URL due to HTTP error. {str(e)}")
        except Exception as e:
            raise PipelineServiceError(f"Error: An unexpected error occurred. {str(e)}")


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
        source_info (dict): A dictionary containing the necessary source URL and other information

        Returns:
            extracted_data_list (list): A list of panda dataframe of extracted data
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
    pipeline_service = PipelineService()

    # load the json file containing source information
    try:
        source_info = pipeline_service.load_json("source_info.json")
    except PipelineServiceError as e:
        print(str(e))
        sys.exit(1)
    
    etl_data_pipeline = DataPipeline(pipeline_service)

    # extract data from multiple sources
    etl_data_pipeline.extract(source_info)

    # combine data from both sources

    # transform data

    # load transformed data into database
    url = source_info["data_sources"][0]["data_urls"][0]["url"]
    # url = "https://geeksforgeeks.org/naveen/"
    output_path = os.path.join(os.getcwd(), "data", "output_bicyle.csv")
    print(url)
    print(output_path)
    try:
        pipeline_service.download_data(url, output_path)
    except PipelineServiceError as e:
        print(str(e))
        sys.exit(1)
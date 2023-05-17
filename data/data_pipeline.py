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
from typing import Dict

# Third party imports

# Self imports
from service_factory import HelperService
from data_extractor import DataExtractor
from data_transformer import DataTransformer
from data_loader import DataLoader


class DataPipeline:
    """
    A class to represent an ETL pipeline.

    Attributes:
        helper_service (HelperService): 
        extractor (DataExtractor): An object of DataExtractor class for extracting data
        transformer (DataTransformer): An object of DataTransformer class for transforming data
        loader (DataLoader): An object of DataLoader class for loading data

    Methods:
        on_extract(source_info: Dict) ->  Dict: Extracts data from multiple sources.
        on_transform(extracted_data: Dict) -> Dict: Transforms the input data by applying necessary transformations.
        on_load(transformed_data: Dict) -> None: Loads transformed data into database.
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
    
    def on_extract(self, source_info: Dict) ->  Dict:
        """
        Extracts data from multiple sources.

        Parameters:
            source_info (dict): A dictionary containing the necessary source URL and other information.

        Returns:
            Dictionary: A dictionary containing information of extracted data.
        """
        self.extractor.source_info = source_info
        self.extractor.extract()

        return self.extractor.extracted_data

    def on_transform(self, extracted_data: Dict) -> Dict:
        """
        Transforms the input data by applying necessary transformations.

        Parameters:
            extracted_data (pd.DataFrame): A panda dataframe of all the extracted data.

        Returns:
            transformed_data (dict): A dict that contains transformed data.
        """
        self.transformer.extracted_data = extracted_data
        self.transformer.transform()

        return self.transformer.transformed_data

    def on_load(self, transformed_data: Dict) -> None:
        """
        Loads transformed data into database.

        Parameters:
            transformed_data (dict): A dict that contains transformed data.
        
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
        # load the source information from the json file
        source_info = helper_service.load_json("source_info.json")
        
        # extract data from multiple sources
        print("\n{} {} {}".format(20*"-", "Extract: data extraction from the source initiated", 20*"-"))
        extracted_data = self.on_extract(source_info)
        print("{} {} {}\n".format(20*"-", "Extract: data extraction from the source ended", 20*"-"))
        
        # read, transform and merge data from both sources
        print("\n{} {} {}".format(20*"-", "Transform: data transformation from extracted data initiated", 20*"-"))
        transformed_data = self.on_transform(extracted_data)
        print("{} {} {}\n".format(20*"-", "Transform: data transformation from extracted data ended", 20*"-"))

        # load transformed data into database
        # loaded_data = self.on_load(transformed_data)


if __name__ == '__main__':
    helper_service = HelperService() # created a object of HelperService
    data_extractor = DataExtractor() # created a object of DataExtractor
    data_transformer = DataTransformer() # created a object of DataTransformer
    data_loader = DataLoader() # created a object of DataLoader

    # created a object of DataPipeline using helper service, extractor, transformer and loader object
    etl_data_pipeline = DataPipeline(
        helper_service = helper_service,
        extractor = data_extractor,
        transformer = data_transformer,
        loader = data_loader
    )

    etl_data_pipeline.run_pipeline() # run the ETL pipeline

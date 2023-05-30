"""
Script Name: main.py
Script Description: This script run the whole ETL pipeline
Author: Sujit Debnath
Author Email: sujit.debnath.bd@gmail.com
University: Friedrich-Alexander University Erlangen-Nuremberg
Course: Data Engineering (AMSE/SAKI)
Semester: SS2023
"""


# Python imports

# Third party imports

# Self imports
from pipelines.data_pipeline import DataPipeline
from utils.service_factory import HelperService
from etl.extract.data_extractor import DataExtractor
from etl.transform.data_transformer import DataTransformer
from etl.load.data_loader import DataLoader


if __name__ == '__main__':
    # created a object of DataPipeline using helper service, extractor, transformer and loader object
    etl_data_pipeline = DataPipeline(
        helper_service = HelperService(),
        extractor = DataExtractor(),
        transformer = DataTransformer(),
        loader = DataLoader()
    )

    etl_data_pipeline.run_pipeline() # run the ETL pipeline
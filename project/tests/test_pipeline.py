# Python imports
import unittest
import json
import pickle
import sqlite3

# Third party imports
import pandas as pd
from pandas.testing import assert_frame_equal

# Self imports
from config.config_var import *
from pipelines.data_pipeline import DataPipeline
from utils.service_factory import HelperService
from etl.extract.data_extractor import DataExtractor
from etl.transform.data_transformer import DataTransformer
from etl.load.data_loader import DataLoader


class TestPipeline(unittest.TestCase):

    # HelperService component testing
    def test_helper_service(self):
        with open(SOURCE_INFO_PATH, 'r') as file:
            expected_data = json.load(file)

        helper_service = HelperService()
        hs_load_json = helper_service.load_json(SOURCE_INFO_PATH)

        self.assertEqual(hs_load_json, expected_data)
    
    # DataExtractor component testing
    def test_data_extractor(self):
        expected_data = {
            'Mobilithek': [
                ('2009', 'mobilithek_bicycle_traffic_2009.csv'),
                ('2010', 'mobilithek_bicycle_traffic_2010.csv'),
                ('2011', 'mobilithek_bicycle_traffic_2011.csv'),
                ('2012', 'mobilithek_bicycle_traffic_2012.csv'),
                ('2013', 'mobilithek_bicycle_traffic_2013.csv'),
                ('2014', 'mobilithek_bicycle_traffic_2014.csv'),
                ('2015', 'mobilithek_bicycle_traffic_2015.csv'),
                ('2016', 'mobilithek_bicycle_traffic_2016.csv'),
                ('2017', 'mobilithek_bicycle_traffic_2017.csv'),
                ('2018', 'mobilithek_bicycle_traffic_2018.csv'),
                ('2019', 'mobilithek_bicycle_traffic_2019.csv'),
                ('2020', 'mobilithek_bicycle_traffic_2020.csv'),
                ('2021', 'mobilithek_bicycle_traffic_2021.csv'),
                ('2022', 'mobilithek_bicycle_traffic_2022.csv')
            ],
            'Meteostat': [
                ('10513', 'Köln-Bonn Airport', 'meteostat_weather_data_10513_Köln-Bonn Airport.csv.gz'),
                ('D2968', 'Köln-Stammheim', 'meteostat_weather_data_D2968_Köln-Stammheim.csv.gz')
            ]
        }

        with open(SOURCE_INFO_PATH, 'r') as file:
            source_info = json.load(file)
        
        data_extractor = DataExtractor()
        data_extractor.source_info = source_info
        data_extractor.extract()
        extracted_data = data_extractor.extracted_data

        self.assertEqual(extracted_data, expected_data)
    
    # DataTransformer component testing
    def test_data_transformer(self):
        with open(os.path.join(os.getcwd(), 'tests', 'transformed_data.pkl'), 'rb') as file:
            expected_data = pickle.load(file)
        
        extracted_data = {
            'Mobilithek': [
                ('2009', 'mobilithek_bicycle_traffic_2009.csv'),
                ('2010', 'mobilithek_bicycle_traffic_2010.csv'),
                ('2011', 'mobilithek_bicycle_traffic_2011.csv'),
                ('2012', 'mobilithek_bicycle_traffic_2012.csv'),
                ('2013', 'mobilithek_bicycle_traffic_2013.csv'),
                ('2014', 'mobilithek_bicycle_traffic_2014.csv'),
                ('2015', 'mobilithek_bicycle_traffic_2015.csv'),
                ('2016', 'mobilithek_bicycle_traffic_2016.csv'),
                ('2017', 'mobilithek_bicycle_traffic_2017.csv'),
                ('2018', 'mobilithek_bicycle_traffic_2018.csv'),
                ('2019', 'mobilithek_bicycle_traffic_2019.csv'),
                ('2020', 'mobilithek_bicycle_traffic_2020.csv'),
                ('2021', 'mobilithek_bicycle_traffic_2021.csv'),
                ('2022', 'mobilithek_bicycle_traffic_2022.csv')
            ],
            'Meteostat': [
                ('10513', 'Köln-Bonn Airport', 'meteostat_weather_data_10513_Köln-Bonn Airport.csv.gz'),
                ('D2968', 'Köln-Stammheim', 'meteostat_weather_data_D2968_Köln-Stammheim.csv.gz')
            ]
        }

        data_transformer = DataTransformer()
        data_transformer.extracted_data = extracted_data
        data_transformer.transform()
        transformed_data = data_transformer.transformed_data

        assert_frame_equal(transformed_data["Mobilithek"], expected_data["Mobilithek"])
        assert_frame_equal(transformed_data["Meteostat"], expected_data["Meteostat"])
    
    # DataLoader component testing
    def test_data_loader(self):
        with open(os.path.join(os.getcwd(), 'tests', 'transformed_data.pkl'), 'rb') as file:
            transformed_data = pickle.load(file)
        
        data_loader = DataLoader()
        data_loader.transformed_data = transformed_data
        data_loader.load()

        conn = sqlite3.connect(DB_PATH)
        expected_data_t1 = pd.read_sql_query("SELECT * FROM mobilithek_bicycle_traffic", conn)
        expected_data_t2 = pd.read_sql_query("SELECT * FROM meteostat_weather_data", conn)
        conn.close()

        assert_frame_equal(transformed_data["Mobilithek"], expected_data_t1)
        assert_frame_equal(transformed_data["Meteostat"], expected_data_t2)

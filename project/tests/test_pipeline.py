# Python imports
import unittest
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


class TestSystem(unittest.TestCase):

    # System Testing: whole ETL pipeline
    def test_data_pipeline(self):
        etl_data_pipeline = DataPipeline(
            helper_service = HelperService(),
            extractor = DataExtractor(),
            transformer = DataTransformer(),
            loader = DataLoader()
        )

        etl_data_pipeline.run_pipeline()

        self.assertTrue(os.path.exists(DB_PATH))

        conn = sqlite3.connect(DB_PATH)

        expected_row_counts = {
            'mobilithek_bicycle_traffic': 168,
            'meteostat_weather_data': 165
        }

        for table_name, expected_row_count in expected_row_counts.items():
            db_data = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
            self.assertEqual(len(db_data), expected_row_count)
        
        conn.close()

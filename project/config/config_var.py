import os

BASE_DIR = os.getcwd()
SOURCE_INFO_PATH = os.path.join(BASE_DIR, "config", "source_info.json")
DOWNLOADED_RAW_FILE_PATH = os.path.join(BASE_DIR, "data", "raw")
DB_PATH = "fau_data_engineering_ss23.sqlite"
# DB_PATH = os.path.join(BASE_DIR, "data", "processed", "fau_data_engineering_ss23.sqlite")
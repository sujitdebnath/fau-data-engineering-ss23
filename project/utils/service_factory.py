# Python imports
from typing import Dict, Union
import json, sys

# Third party imports

# Self imports


class HelperService:
    """
    A class for providing external services for implementing ETL pipeline

    Attributes:
        None

    Methods:
        load_json(file_path: str) -> Dict/None: Loads a JSON file as a dictionary.
    """

    def __init__(self) -> None:
        pass

    def load_json(self, file_path: str) -> Union[Dict, None]:
        """
        Loads a JSON file as a dictionary.

        Parameters:
            file_path (str): Path to the JSON file.

        Returns:
            data (dict/none): Loaded JSON data as a dictionary.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            print(f"Succeed: JSON loaded successfully")
            return data
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON data in file '{file_path}'.")
            sys.exit(1)
        except Exception as e:
            print(f"Error: An unexpected error occurred. {str(e)}")
            sys.exit(1)

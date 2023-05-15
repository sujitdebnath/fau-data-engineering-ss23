# Python imports
import requests

# Third party imports

# Self imports


class DataExtractor:
    """
    A class to represent the data extractor of an ETL pipeline.

    Attributes:
        source_info (dict): A dictionary containing the necessary source URL and other information.
        extracted_data (list): A list of strings which represent the raw data file path of extracted data
    
    Methods:
        extract() ->  None: Extracts data from multiple sources.
        _download_data(url: str, output_path: str) -> None: Downloads data from the specified URL and saves it to the output path.
    """

    def __init__(self) -> None:
        self.source_info = None
        self.extracted_data = list()

    def extract(self) -> None:
        """
        Extracts data from multiple sources.

        Parameters:
            None

        Returns:
            None
        """
        pass

    def _download_data(self, url: str, output_path: str) -> None:
        """
        Downloads data from the specified URL and saves it to the output path.

        Parameters:
            url (str): The URL from which to download the data.
            output_path (str): The path where the downloaded data will be saved.
        
        Returns:
            None
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an exception if the request was unsuccessful

            with open(output_path, 'wb') as file:
                file.write(response.content)

            print(f"Succeed: Data downloaded successfully and saved to: {output_path}")
        except requests.exceptions.ConnectionError as e:
            print(f"Error: Failed to download data from URL due to Connection error.")
        except requests.exceptions.HTTPError as e:
            print(f"Error: Failed to download data from URL due to HTTP error. {str(e)}")
        except Exception as e:
            print(f"Error: An unexpected error occurred. {str(e)}")
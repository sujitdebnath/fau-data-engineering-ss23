# Python imports
import sqlite3
import sys

# Third party imports

# Self imports


class DataLoader:
    """
    A class to represent the data loader of an ETL pipeline.

    Attributes:
        transformed_data (dict): A dict that contains transformed data.
    
    Methods:
        load() -> None: Loads transformed data into database.
    """

    def __init__(self) -> None:
        self.transformed_data = None

    def load(self) -> None:
        """
        Loads transformed data into database.

        Parameters:
            None
        
        Returns:
            None
        """
        try:
            # connect to the database
            conn = sqlite3.connect('fau_data_engineering_ss23.sqlite')
            print(f"Succeed: Database created successfully")

            # insert data into the database
            for source, source_merged_df in self.transformed_data.items():
                if source == "Mobilithek":
                    table_name = source.lower() + "_bicycle_traffic"
                elif source == "Meteostat":
                    table_name = source.lower() + "_weather_data"
                
                source_merged_df.to_sql(table_name, conn, if_exists='replace', index=False)
                print(f"Succeed: {source} data source inserted into the database successfully")
            
            # close the connection
            conn.close()
        except sqlite3.Error as e:
            print(f"Error: An error occurred during table population: {str(e)}")
            sys.exit(1)

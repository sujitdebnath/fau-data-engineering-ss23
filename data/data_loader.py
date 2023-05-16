# Python imports

# Third party imports

# Self imports


class DataLoader:
    """
    A class to represent the data loader of an ETL pipeline.

    Attributes:
        transformed_data (pd.DataFrame): A panda dataframe of transformed data.
    
    Methods:
        load(self) -> None: Loads transformed data into database.
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
        pass

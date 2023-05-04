from abc import ABC, abstractmethod
import pandas as pd


class Isave(ABC):

    def __init__(self, import_data: pd.DataFrame):
        """
         :param import_data: take in a pandas dataframe and saves it when implemented
        """
        self.import_data = import_data

    @abstractmethod
    def save(self):
        pass

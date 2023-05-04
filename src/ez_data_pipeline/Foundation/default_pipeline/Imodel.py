from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
from typing import Union


class Imodel(ABC):
    def __init__(self, processed_data: Union[pd.DataFrame, np.ndarray]):
        """
        :param processed_data: the data needs to be CLEAN
        """
        self.processed_data = processed_data

    @abstractmethod
    def run_model(self) -> pd.DataFrame:
        pass

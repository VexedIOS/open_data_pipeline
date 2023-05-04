from abc import ABC, abstractmethod
from ez_data_pipeline.Foundation import utils


class IImporter(ABC):
    """
    Generalized Interface for changing the source and import to accommodate the return_data abstract method
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _import(self):
        pass

    @abstractmethod
    def find_asset_class(self) -> str:
        pass

    @abstractmethod
    def return_data(self) -> utils.ImportData:
        pass
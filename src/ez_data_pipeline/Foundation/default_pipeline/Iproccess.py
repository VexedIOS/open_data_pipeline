from abc import ABC, abstractmethod, ABCMeta
from ez_data_pipeline.Foundation.utils import ImportData


class Processor(ABC):
    @abstractmethod
    def process(self, import_data: ImportData) -> ImportData:
        pass

    def __str__(self):
        return self.__class__.__name__


class ProcessPipeline:

    def __init__(self, import_data: ImportData):
        """
        :param import_data: data that is shared with all processes
        """
        self.import_data = import_data
        self.processed_data = None

    def run_processes(self):
        """
        Runs all abc methods future version might require more robust class filtering
        """
        for i in dir(self.__class__):
            attr = getattr(self.__class__, i)
            if type(attr) is ABCMeta:
                self.processed_data = attr().process(self.import_data)

    def __str__(self):
        list_methods = []
        for i in dir(self.__class__):
            attr = getattr(self.__class__, i)
            if type(attr) is ABCMeta:
                list_methods.append(i)

        return "".join[list_methods]

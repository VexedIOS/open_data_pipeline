from ez_data_pipeline.Foundation.default_pipeline.Imodel import Imodel
from ez_data_pipeline.Foundation.default_pipeline.IproccessMethod import ProcessingMethod


class ModelPipeline:
    """
    This combines all previous classes Imodel, and ProcessingMethod
    to return dataframe for prediction
    """
    def __init__(self, data_model: Imodel, data_processing: ProcessingMethod):
        """
        :param data_model: Creates and runs model
        :param data_processing: The processing method combines Import -> Process -> Save
        """
        self.data_model = data_model
        self.data_processing = data_processing
        self.result = None

    def run_pipeline(self):
        """
        runs the entire pipeline and return the result as well save it
        :return:
        """
        self.data_processing.run_data_proccess()
        self.data_model =self.data_model(self.data_processing.process_data.pd_data)
        self.result = self.data_model.run_model()
        return self.result
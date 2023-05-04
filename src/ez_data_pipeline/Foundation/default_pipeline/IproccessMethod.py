from ez_data_pipeline.Foundation.default_pipeline.Isave import Isave
from ez_data_pipeline.Foundation.default_pipeline.Iproccess import ProcessPipeline
from ez_data_pipeline.Foundation.default_pipeline.Iimporter import IImporter


# Any way to type-hint
# Fix later
class ProcessingMethod:

    def __init__(self, data_importer: IImporter, process_pipeline: ProcessPipeline, saver: Isave, ticker: str):
        """
        dataimporter: Importer
        dateprocessor: Iprocess
        ticker_save: ISave
        """
        self.data_importer = data_importer
        self.process_pipeline = process_pipeline
        self.saver = saver
        self.ticker = ticker
        self.process_data = None

    def run_data_proccess(self):
        """
        Combines import -> process -> save classes and pre-processes data
        :return:
        """
        data_importer = self.data_importer(self.ticker)
        import_data = data_importer.return_data()
        pipeline_processor = self.process_pipeline(import_data)
        pipeline_processor.run_processes()
        self.saver(pipeline_processor.processed_data).save()
        self.process_data = pipeline_processor.processed_data
        return pipeline_processor.processed_data

# protocol

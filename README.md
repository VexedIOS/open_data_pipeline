
# Open Data Pipeline

Object-oriented  library to quickly deploy and test data pipelines and models 
# Installing Library 
`pip install ez-data-pipeline`

# General Contribution Guidelines 

Create a feature branch, try to merge by end of day in order to avoid conflict.
Every major commit will have associated test cases so make sure you use TDD.

# Building first pipeline

### Required Imports
```
import pandas as pd
import yfinance
from ez_data_pipeline.Foundation.default_pipeline.Iimporter import IImporter
from ez_data_pipeline.Foundation.default_pipeline.Imodel import Imodel
from ez_data_pipeline.Foundation.default_pipeline.Ipipeline import ModelPipeline
from ez_data_pipeline.Foundation.default_pipeline.Iproccess import ProcessPipeline, Processor
from ez_data_pipeline.Foundation.default_pipeline.IproccessMethod import ProcessingMethod
from ez_data_pipeline.Foundation.default_pipeline.Isave import Isave
from ez_data_pipeline.Foundation.utils import ImportData, AssetClass 
```
###  Creating Importing class 
```
class yf_Import(IImporter):

    def __init__(self, ticker: str):
        self.ticker = ticker
        self.data_ticker = yfinance.Ticker(self.ticker)
        self.data = self.data_ticker.history("max")

    def _import(self) -> pd.DataFrame:
        return self.data

    def find_asset_class(self) -> str:
        return self.data_ticker.info['quoteType']

    def return_data(self) -> ImportData:
        data_dict = {"EQUITY": AssetClass.Stock, "ETF": AssetClass.ETF}
        yf_asset_type = self.find_asset_class()
        return ImportData(self._import(), data_dict[yf_asset_type])

    def __str__(self):
        return f"TICKER: {str(self.data)}"

    def __repr__(self):
        return f"yf_Import({self.ticker})"
```
### Process Pipeline
```
class ProcessPipeline(ProcessPipeline):
    # Add processor to list
    class AddProcessor(Processor):
        def process(self, import_data: ImportData) -> ImportData:
            import_data.pd_data = import_data.pd_data + 1
            return import_data

    # Add processor to list
    class RemoveRowProcessor(Processor):
        def process(self, import_data: ImportData) -> ImportData:
            import_data.pd_data = import_data.pd_data.drop("High", axis=1)
            return import_data

    class MakeRandomOperation(Processor):
        def process(self, import_data: ImportData) -> ImportData:
            import_data.pd_data = import_data.pd_data + 2
            return import_data

```
### Creating Saving Class
```
class CSVSave(Isave):
    def save(self):
        print("saved")
        
```
### Creating Process Method
This method is meant to isolate the pre-processing section of model development to easily test it for a production enviroment
```
pm = ProcessingMethod(yf_Import, ProcessPipeline, CSVSave, "SPY")
```
### Creating Model 
```
class LinearModel(Imodel):
    """Write you cool Model here"""
    def run_model(self) -> pd.DataFrame:
        """Run your cool Model here"""
        return self.processed_data
```
### Creating Full Pipeline

```
test_pipeline = ModelPipeline(data_model=LinearModel, data_processing=pm)
test_pipeline.run_pipeline()

print(test_pipeline.result)
```

# Full Example
```
import pandas as pd
import yfinance
from ez_data_pipeline.Foundation.default_pipeline.Iimporter import IImporter
from ez_data_pipeline.Foundation.default_pipeline.Imodel import Imodel
from ez_data_pipeline.Foundation.default_pipeline.Ipipeline import ModelPipeline
from ez_data_pipeline.Foundation.default_pipeline.Iproccess import ProcessPipeline, Processor
from ez_data_pipeline.Foundation.default_pipeline.IproccessMethod import ProcessingMethod
from ez_data_pipeline.Foundation.default_pipeline.Isave import Isave
from ez_data_pipeline.Foundation.utils import ImportData, AssetClass


# Creating import method
class yf_Import(IImporter):

    def __init__(self, ticker: str):
        self.ticker = ticker
        self.data_ticker = yfinance.Ticker(self.ticker)
        self.data = self.data_ticker.history("max")

    def _import(self) -> pd.DataFrame:
        return self.data

    def find_asset_class(self) -> str:
        return self.data_ticker.info['quoteType']

    def return_data(self) -> ImportData:
        data_dict = {"EQUITY": AssetClass.Stock, "ETF": AssetClass.ETF}
        yf_asset_type = self.find_asset_class()
        return ImportData(self._import(), data_dict[yf_asset_type])

    def __str__(self):
        return f"TICKER: {str(self.data)}"

    def __repr__(self):
        return f"yf_Import({self.ticker})"


# Define the process pipeline
class ProcessPipeline(ProcessPipeline):
    # Add processor to list
    class AddProcessor(Processor):
        def process(self, import_data: ImportData) -> ImportData:
            import_data.pd_data = import_data.pd_data + 1
            return import_data

    # Add processor to list
    class RemoveRowProcessor(Processor):
        def process(self, import_data: ImportData) -> ImportData:
            import_data.pd_data = import_data.pd_data.drop("High", axis=1)
            return import_data

    class MakeRandomOperation(Processor):
        def process(self, import_data: ImportData) -> ImportData:
            import_data.pd_data = import_data.pd_data + 2
            return import_data


# Define Save class
class CSVSave(Isave):
    def save(self):
        print("saved")


class LinearModel(Imodel):
    """Write you cool Model here"""
    def run_model(self) -> pd.DataFrame:
        """Run your cool Model here"""
        return self.processed_data


pm = ProcessingMethod(yf_Import, ProcessPipeline, CSVSave, "SPY")

test_pipeline = ModelPipeline(data_model=LinearModel, data_processing=pm)
test_pipeline.run_pipeline()

print(test_pipeline.result)

```
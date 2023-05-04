from typing import Union
import pandas as pd
from dataclasses import dataclass


class AssetClass:
    class ETF: """ ETF Type"""

    class CryptoCurrency: """ CryptoCurrency Type"""

    class Stock: """ Stock Type"""

    class MLP: """ MLP Type"""

    class Forex: """ Forex Type"""

    class NFT: """NFT Type"""


@dataclass
class ImportData:
    pd_data: pd.DataFrame
    asset_class: Union[AssetClass.ETF, AssetClass.Stock, AssetClass.CryptoCurrency, AssetClass.MLP, AssetClass.Forex]

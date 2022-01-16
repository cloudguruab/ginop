from web3 import Web3
from enum import Enum
import os

class MetaFormat(Enum):
    DIFFICULTY: int = 2
    HTTP_PROVIDER = Web3(Web3.HTTPProvider(os.environ.get('ON_CHAIN_URL')))
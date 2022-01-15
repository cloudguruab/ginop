from web3 import Web3
from enum import Enum
from dotenv import load_dotenv
import os

load_dotenv()

class MetaFormat(Enum):
    HTTP_PROVIDER = Web3(Web3.HTTPProvider(os.environ.get('ON_CHAIN_URL')))
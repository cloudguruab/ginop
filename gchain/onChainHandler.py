from web3 import Web3
from dotenv import load_dotenv
from .chainTypes import AdminTypes
import json
import os

load_dotenv()

class Admin:
    
    def __init__(self, name:str):
        self._onChainURL = os.environ.get('ON_CHAIN_URL')
        self.name = name
        
    def __repr__(self):
        return f'<Admin: {self.name} >'
    
    def __str__(self):
        return f'<Admin: {self.name} >'
    
    def __bool__(self):
        if self.name:
            return True
        return False  
     
    @staticmethod
    def grab_provider(ipc):
        my_provider = Web3.IPCProvider(ipc)
        
        if not ipc: 
            return f'No provider address given, ipc is empty'
        
        return my_provider
    
    @staticmethod
    def admin_level():
        """
        Depending on admin level will delegate ipc init
        """
        pass
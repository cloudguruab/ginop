"""handler for connecting to different providers"""

from web3 import Web3
from ..common.constants import MetaFormat


class Controller:
    
    def __init__(self, name:str, admin_level:str):
        """
        configuration of connector instance
        
        :param name: identifier of admin interface
        """
        self.name = name
        
    def __repr__(self):
        return f'<Admin: {self.name} >'
    
    def __str__(self):
        return f'<Admin: {self.name} >'
    
    def __bool__(self):        
        state = MetaFormat.HTTP_PROVIDER.value
        
        if state.isConnected(): 
            print(f'{http_provider} is connected...') #log something
            return True
        
        return False 
    
    def est_conf(self):
        """
        will delegate provider type,.
        
        :rtype profile: dict object for frontend meta data rendered to user
        """
        if Admin.__bool__(self) != False:
            return {"state": "connected..."} 
        
        return {"state": "no connection present"}
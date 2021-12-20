from web3 import Web3
from common.constants import MetaFormat
import json


#handler is responsible for 
# admin settings
# connecting to blockchain
# establishing root behavior for transactions
# establishing root behavior for reading blocks
# establishing root behavior for writing contract

class Admin:
    
    def __init__(self, name:str, admin_level:str):
        """
        configuration of admin instance
        
        :param name: identifier of admin interface
        :param admin_level: permission identifier for users
        """
        self.name = name
        self.admin_level = admin_level
        
    def __repr__(self):
        return f'<Admin: {self.name} >'
    
    def __str__(self):
        return f'<Admin: {self.name} >'
    
    def __bool__(self):        
        state = MetaFormat.HTTP_PROVIDER.value
        
        if state.isConnected(): 
            # print(f'{http_provider} is connected...') #log something
            return state
        
        return False 
    
    def admin_conf(self):
        """
        depending on admin level will delegate provider type,
        grab provider and check against admin level.
        
        :rtype profile: dict object for frontend meta data rendered to user
        """
        if Admin.__bool__(self) != False:
            return {
                "admin": self.name, 
                "permission_level": self.admin_level,
                "state": "connected..."
            } 
        return {
            "admin": self.name,
            "permission_level": self.admin_level,
            "state": "no connection present"
        }
        

class Permission(Admin):
    
    def __init__(self):
        pass
    
    def __repr__(self):
        pass
    
    def __str__(self):
        pass
    
    def readPermission(self):
        pass
    
    def writePermission(self):
        pass
    
    def transactPermission(self):
        pass
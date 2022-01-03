from web3 import Web3
from common.constants import MetaFormat
import json

# handler is responsible for 
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
            return True
        
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
    
    def __init__(self, name, admin_level):
        super().__init__(name, admin_level)
        self.stats = Admin.admin_conf(self)
    
    def __repr__(self):
        return "<Permission: %s>" % self.admin_level
    
    def __str__(self):
        return "<Permission: %s>" % self.admin_level
    
    def readPermission(self): #TODO: -> need to add db and READING smart contract functionality
        permission_level = self.stats["permission_level"]
        state = self.stats["state"]
        
        if state == "connected...":
            if permission_level == "admin":
                print('You have root level privledges')
            elif permission_level == "tenant": 
                print("You have read and some write access")
        else:
            print("No connection present")
    
    def writePermission(self): #TODO: -> need to add db and WRITING smart contract functionality
        permission_level = self.stats["permission_level"]
        state = self.stats["state"]
        
        if state == "connected...":
            if permission_level == "admin":
                print('You have root level privledges')
            elif permission_level == "tenant": 
                print("You have read and some write access")
        else:
            print("No connection present")
    
    def transactPermission(self): #TODO: -> need to add db and SIGNING smart contract functionality
        permission_level = self.stats["permission_level"]
        state = self.stats["state"]
        
        if state == "connected...":
            if permission_level == "admin":
                print('You have root level privledges')
            elif permission_level == "tenant": 
                print("You have read and some write access")
        else:
            print("No connection present")
    
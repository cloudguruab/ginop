"""types for ginop blockchain logic"""

class ChainTypes:
    """
    configuration for blockchain types
    
    g_url: url for lcoal development chain ginop runs on
    chain_address_one: on chain address for sender or receiver of transaction
    chain_address_two: on chain address for sender or receiver of transaction
    gtx: transaction object for chain address connections
    hash: used for grabbing specifc transactions off a particular block
    """
    g_url:str
    chain_address_one:str
    chain_address_two:str
    gtx:dict
    hash:str
    
class AdminTypes:
    """
    configuration for admin level users
    
    name: user identifier for admin using ginop system
    admin_type: chain level permission of admin
    """
    name:str
    admin_type:str
    level:int 
    privileges:str 
    
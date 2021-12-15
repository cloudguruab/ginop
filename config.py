"""configuration class for application"""

import os  
from dotenv import load_dotenv

load_dotenv()

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    DATABASE = None
    
    SIGNATURE = None
    
    GANACHE_URL = None 
    
    ONCHAIN_PRIVATE_KEY = None
    
    
"""configuration class for application"""

import os  
from pathlib import Path

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    PROD_SECRET_KEY = os.environ.get('PROD_SECRET_KEY')
    
    DATABASE = os.environ.get('DATABASE')
    
    PATH = Path(__file__).resolve().parent.parent
    
    SIGNATURE = None
    
    GANACHE_URL = None 
    
    ONCHAIN_PRIVATE_KEY = None
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

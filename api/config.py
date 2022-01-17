"""configuration class for application"""

import os  

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    PROD_SECRET_KEY = os.environ.get('PROD_SECRET_KEY')
    
    DATABASE = os.environ.get('DATABASE')
        
    #assign new variables here
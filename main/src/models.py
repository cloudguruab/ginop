from config import Config
from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

db_string = Config.DATBASE

db = create_engine(db_string)  
base = declarative_base()

class Film(base):  
    __tablename__ = 'ginop'

    id = None
    created_at = None  # TODO:
    signed_at = None  
    signature = None 
    workflow = None  
    # geospacial = bool  
    # sms = bool 
    # biometric = bool

Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)
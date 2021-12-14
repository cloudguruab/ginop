"""Blueprint configuration for server side"""

import os
from flask import Flask

def create_app():
    app = Flask(__name__, static_folder="./static", template_folder="./templates")
    # setup app config TODO:
    # from config import Config import 
    
    # ensure instance folder exists, what is this? TODO:
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass
    
    return app
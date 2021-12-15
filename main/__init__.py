"""configuration for server side"""

import os
from flask import Flask
from config import Config 

def create_app(config_class=Config):
    app = Flask(__name__, static_folder="./static", template_folder="./templates")
    app.config.from_object(config_class)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from main.src import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app
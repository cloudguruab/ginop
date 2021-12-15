"""configuration for server side"""

import os
from flask import Flask, current_app
from config import Config 

def create_app(config_class=Config):
    app = Flask(__name__, static_folder="./static", template_folder="./templates")
    app.config.from_object(config_class)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from .main_app.models import db as gdb
    with app.app_context():
        current_app.config['SQLALCHEMY_DATABASE_URI'] = config_class.DATABASE
        gdb.init_app(app)
        gdb.create_all()

    from main.main_app import bp as main_bp
    app.register_blueprint(main_bp)
        
    return app
"""configuration for server side"""

import os, logging
import logging.config
from flask import Flask, current_app
from config import Config 

def create_app(config_class=Config):
    app = Flask(__name__, static_folder="./static", template_folder="./templates")
    app.config.from_object(config_class)
    logging.config.fileConfig('logging.conf')

    # create logger
    logger = logging.getLogger('main_logger')
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        logger.info("instance folder %s already exist" % app.instance_path)
        pass
    
    from .main_app.models import db as gdb
    with app.app_context():
        current_app.config['SQLALCHEMY_DATABASE_URI'] = config_class.DATABASE
        gdb.init_app(app)
        gdb.create_all()

    from main.main_app import bp as main_bp
    app.register_blueprint(main_bp)
        
    logger.info('ginop boot complete...')
    return app


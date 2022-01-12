"""configuration for server side"""

import os, logging
from flask import Flask, current_app
from config import Config 

def create_app(config_class=Config):
    app = Flask(__name__, static_folder="./static", template_folder="./templates")
    app.config.from_object(config_class)

    # create logger
    logger = logging.getLogger(__name__)
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        logger.info("instance folder %s already exist" % app.instance_path)
        pass

    from main.main_app import bp as main_bp
    app.register_blueprint(main_bp)
        
    return app


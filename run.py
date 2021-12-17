from main import create_app
import logging
import logging.config
import yaml
from os.path import join, dirname, realpath

def manager():
    """
    manager for application logging
    """
    #parse yaml file
    config_path = join(dirname(realpath(__file__)), 'log/conf.yml')
    config = yaml.safe_load(open(config_path))

    #configure loggging
    log_config = config['logging']
    logging.config.dictConfig(log_config) 
    logger = logging.getLogger(__name__)
    
app = create_app()

if __name__ == '__main__':
    manager()
    app.run(port=5000, debug=True)
    

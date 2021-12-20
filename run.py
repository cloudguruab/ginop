from main import create_app
import logging
import logging.config
import yaml
import os 

def manager():
    """
    manager for application logging
    """
    #parse yaml file
    path = os.path.dirname(os.path.realpath(__file__))
    loggingConf = f"{path}/log/conf.yml"
    config = yaml.safe_load(loggingConf)

    #configure loggging
    log_config = config['logging']
    logging.config.dictConfig(log_config) 
    logger = logging.getLogger(__name__)
    
app = create_app()

if __name__ == '__main__':
    manager()
    app.run(port=5000, debug=True)
    

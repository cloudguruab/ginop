from main import create_app
import logging
import logging.config

app = create_app()

if __name__ == '__main__':
    # logging.config.fileConfig('logging.conf')
    app.run(port=5000, debug=True)
    

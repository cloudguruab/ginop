import logging, time, json, os, datetime
import logging.config
from main.main_app import bp
from flask import render_template, redirect
from .models import GinopDB

# log_file_path = os.path.join()
logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('main_logger')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')


#initial route
@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')    

@bp.route('/clock-in', methods=[''])
def clock_in():
    # time clocked in 
    # nonce generated
    # transaction is initialized but not completed  
    pass

@bp.route('/clock-out')
def clock_out():
    # time clocked out 
    # verify nonce exist for specific transaction
    # read what transactions exists
    # transaction is completed 
    pass
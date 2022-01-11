import logging, time, json, os, datetime
from main.main_app import bp
from flask import render_template, redirect
from .models import GinopDB

logger = logging.getLogger(__name__)

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
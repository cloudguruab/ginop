import logging, time, json, os, datetime
from main.src import bp
from flask import render_template, redirect


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
    # transaction is completed 
    pass
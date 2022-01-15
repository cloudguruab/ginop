import logging, time, json, os, datetime
from main.main_app import bp
from flask import render_template, redirect
import os.path, sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from blockchain.private import chain

logger = logging.getLogger(__name__)
blockchain = chain.Blockchain()

#initial route
@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')    

@bp.route('/chain', methods=['GET'])
def private_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})
    
@bp.route('/register', methods=['GET', 'POST'])
def register(): #TODO:
    return render_template('index.html')
    
# @bp.route('/clock-in', methods=[''])
# def clock_in():
    # time clocked in 
    # nonce generated
    # transaction is initialized but not completed  
#     pass

# @bp.route('/clock-out')
# def clock_out():
    # time clocked out 
    # verify nonce exist for specific transaction
    # read what transactions exists
    # transaction is completed 
#     pass
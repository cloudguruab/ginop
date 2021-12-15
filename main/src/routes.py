import logging, time, json, os, datetime
from main.src import bp
from flask import render_template, redirect


#initial route
@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')    

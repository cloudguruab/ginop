import logging, time, json, os, datetime
from flask import render_template, redirect
from ..database import models

#initial route
@app.route('/', methods=['GET', 'POST'])
def index():
    render_template('index.html')
    

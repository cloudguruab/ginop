''' Blueprint for main application functionality. '''
from flask import Blueprint

bp = Blueprint('src', __name__, template_folder='../templates')

from main.src import routes
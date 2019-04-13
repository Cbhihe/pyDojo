'''
Module string
'''

from flask import Blueprint, render_template
from models import get_list

views = Blueprint('views', __name__)


@views.route('/')
def index():
    '''
    doc string
    '''
    return render_template('index.html')


@views.route('/')
def list():
    '''
    doc string
    '''
    token_list = get_list()
    return render_template('list.html', token_list=token_list)

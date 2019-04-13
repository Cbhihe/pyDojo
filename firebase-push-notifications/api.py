''' 
Module string
'''

from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from models import db, User

api = Blueprint('api', __name__)

@api.route('/save-token', methods=['POST'])
def save_token():
    '''
    doc string
    '''
    token = request.json.get('token')
    user = User(token=token)

    try:
        db.session.add(user)
        db.session.commit()

    except SQLAlchemiyError:
        return jsonify({'error': SQLAlchemyError.__name__})

    return jsonify({'tokeni': token})

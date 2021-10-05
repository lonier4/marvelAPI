from flask import Blueprint, jsonify
from app.models import Marvel, db

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/characters', methods=['GET'])
def characters():
    """
    [GET] /api/characters
    Returns a list of all marvel characters in the database
    """
    characters = {m.id:m.to_dict() for m in Marvel.query.all()}
    # dictionary comprehension returns m.id as key and m.to_dict() as value
    print(characters)
    return jsonify(characters)
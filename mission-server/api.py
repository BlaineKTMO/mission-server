import flask
import json

from flask import (
        Blueprint, jsonify, request
)

result = {"result": False}

bp = Blueprint('api', __name__, url_prefix='/api')

example_mission = {
        "Waypoint": 'Station 1',
        "Zone": "1",
        "Distance": 10
        }

@bp.route('/mission', methods=['GET'])
def send_mission():
    return jsonify(example_mission)

@bp.route('/mission_result', methods=['GET', 'POST'])
def mission_result():
    if flask.request.method == 'POST':
        global result
        result = request.get_json() 
        
        response = jsonify(result)
        response.status_code = 200
        return response
    else:
        return result

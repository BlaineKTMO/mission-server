from flask import (
        Blueprint, jsonify
)

bp = Blueprint('api', __name__, url_prefix='/api')

example_mission = {
        "Waypoint": 'Station 1',
        "Zone": 1,
        }

@bp.route('/mission', methods=['GET'])
def send_mission():
    return jsonify(example_mission)

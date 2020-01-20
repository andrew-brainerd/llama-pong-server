import flask
from flask import jsonify
from pong_service import PongService
import datetime
import json

app = flask.Flask(__name__)
app.config['DEBUG'] = True
pong_service = PongService()


@app.route('/api/time', methods=['GET'])
def get_test():
    current_time = str(datetime.datetime.now())
    data = json.dumps({'time': current_time})
    return jsonify(data)


@app.route('/api/players/<string:id>', methods=['GET'])
def get_player(id):
    data = pong_service.get_player(id)
    return jsonify(data)


@app.route('/api/players/<string:id>', methods=['POST'])
def create_player(id):
    data = pong_service.create_player(id)
    print(data)
    return jsonify(data)


@app.route('/api/players', methods=['GET'])
def get_players():
    data = pong_service.get_players()
    return jsonify(data)

import flask
from flask import jsonify, request
from pong_service import PongService
import datetime
import json

app = flask.Flask(__name__)
app.config['DEBUG'] = True
pong_service = PongService()

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/api/time', methods=['GET'])
def get_test():
    current_time = str(datetime.datetime.now())
    data = json.dumps({'time': current_time})
    return jsonify(data)


@app.route('/api/players/<string:id>', methods=['GET'])
def get_player(id):
    data = pong_service.get_player(id)
    return jsonify(data)


@app.route('/api/players', methods=['POST'])
def create_player():
    data = pong_service.create_player(request.json)
    return jsonify(data)


@app.route('/api/players', methods=['GET'])
def get_players():
    data = pong_service.get_players()
    return jsonify(data)

@app.route('/api/games', methods=['POST'])
def create_new_game():
    data = pong_service.create_new_game(request.json)
    return jsonify(data)

#app.run()

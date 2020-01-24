import flask
from flask import jsonify, request, make_response
from pong_service import PongService
import datetime
import json
from exception import InvalidUsage

app = flask.Flask(__name__)
app.config['DEBUG'] = True
pong_service = PongService()

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = make_response(jsonify(error.to_dict()), error.status_code)
    return response

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

@app.route('/api/games/unfinished', methods=['GET'])
def get_unfinished_games():
    data = pong_service.get_unfinished_games()
    return jsonify(data)

@app.route('/api/games/<string:id>', methods=['GET'])
def get_game(id):
    data = pong_service.get_game(id)
    return jsonify(data)

@app.route('/api/games/<string:id>', methods=['PUT'])
def update_game(id):
    pong_service.update_game(id, request.json)
    data = {'success':True}
    print ('hit update_game finish')
    return jsonify(data), 200, {'ContentType':'application/json'}

#app.run()

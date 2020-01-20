import flask
from flask import jsonify
from pong_service import PongService

app = flask.Flask(__name__)
app.config["DEBUG"] = True
pong_service = PongService()

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

app.run()
from pymongo import MongoClient
import os
import uuid
import datetime

PLAYERS_COLLECTION = 'players'
GAMES_COLLECTION = 'games'
SCORE = 'score'
GAME_ID = 'gameId'

class PongRepository():
    def __init__(self):
        user = os.getenv('MONGO_USER')
        password = os.getenv('MONGO_PASSWORD')
        address = os.getenv('MONGO_ADDRESS')
        self.database = str(os.getenv('MONGO_DATABASE'))
        self.client = MongoClient(
            f'mongodb://{user}:{password}@{address}/{self.database}?retryWrites=false')

    def get_player(self, id):
        db = self.client[self.database]
        collection = db[PLAYERS_COLLECTION]
        data = collection.find_one({'playerId': id}, {'_id': False})
        return data

    def create_player(self, name):
        db = self.client[self.database]
        collection = db[PLAYERS_COLLECTION]
        guid = str(uuid.uuid4())
        data = {
            'name': name,
            'playerId': guid
        }
        collection.insert_one(data)
        data['_id'] = str(data['_id'])
        return data

    def get_players(self):
        print ("hit me baby one more time")
        db = self.client[self.database]
        collection = db[PLAYERS_COLLECTION]
        print ("hit me baby two more times")
        data = collection.find_one({}, {'_id': False})
        return data

    def create_new_game(self, id1, id2):
        db = self.client[self.database]
        collection = db[GAMES_COLLECTION]
        guid = str(uuid.uuid4())
        current_time = str(datetime.datetime.now())
        guid1 = str(uuid.uuid4())
        guid2 = str(uuid.uuid4())
        print (f'guid2 = {guid2}')
        data = {
            'gameId': guid,
            'player1': {
                'playerId': id1,
                'score': 0
            },
            'player2': {
                'playerId': id2,
                'score': 0
            },
            'timeStarted': current_time,
            'timeFinished': None
        }
        collection.insert_one(data)
        return_data = {
            "gameId": guid
        }
        return return_data

    def get_game(self, game_id):
        db = self.client[self.database]
        collection = db[GAMES_COLLECTION]
        data = collection.find_one({GAME_ID: game_id}, {'_id': False})
        return data

    def update_game(self, game_id, player1, player2):
        db = self.client[self.database]
        collection = db[GAMES_COLLECTION]
        collection.update_one({GAME_ID: game_id}, {'$set': {
            'player1': {
                'playerId': player1['playerId'],
                'score': player1[SCORE]
            },
            'player2': {
                'playerId': player2['playerId'],
                'score': player2[SCORE]
            }
        }})
        
        

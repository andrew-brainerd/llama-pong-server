from pymongo import MongoClient
import os

PLAYERS_COLLECTION = 'players'


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
        collection.find({'playerId': id})
        data = {'name': 'fillmore'}
        return data

    def create_player(self, id):
        db = self.client[self.database]
        collection = db[PLAYERS_COLLECTION]
        data = {
            'name': 'fillmore'
        }
        collection.insert_one(data)
        print(data)
        print(data['name'])
        data['_id'] = str(data['_id'])

        return data

    def get_players(self):
        data = {'name': 'fillmore'}
        return data

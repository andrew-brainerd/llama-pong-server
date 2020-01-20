from pymongo import MongoClient
import os


class PongRepository():
    def __init__(self):
        user = os.getenv('MONGO_USER')
        password = os.getenv('MONGO_PASSWORD')
        address = os.getenv('MONGO_ADDRESS')
        database = os.getenv('MONGO_DATABASE')
        self.client = MongoClient(f'mongodb://{user}:{password}@{address}/{database}?retryWrites=false')

    def get_player(self, id):
        db = self.client.heroku_xwp0v8x7
        collection = db['players']
        collection.find('')
        data = {
            'name': 'fillmore'
        }
        return data

    def create_player(self, id):
        db = self.client.heroku_xwp0v8x7
        collection = db['players']
        data = {
            'name': 'fillmore'
        }
        collection.insert_one(data)
        print(data)
        print(data['name'])
        data['_id'] = str(data['_id'])
        
        return data

    def get_players(self):
        data = {
            'name': 'fillmore'
        }
        return data
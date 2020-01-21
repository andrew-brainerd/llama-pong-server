from pong_repository import PongRepository 
import json

class PongService():
    def __init__(self):
        self.pong_repo = PongRepository()

    def get_player(self, id):
        return self.pong_repo.get_player(id)

    def create_player(self, body):
        player_name = body['name']
        return self.pong_repo.create_player(player_name)

    def get_players(self):
        return self.pong_repo.get_players()

    def create_new_game(self, body):
        player1 = body['player1']
        player2 = body['player2']
        if 'playerId' in player1:
            id1 = player1['playerId']
        else:
            id1 = '00000000-0000-0000-0000-000000000000'
        if 'playerId' in player2:
            id2 = player2['playerId']
        else:
            id2 = '00000000-0000-0000-0000-000000000000' 
        return self.pong_repo.create_new_game(id1, id2)

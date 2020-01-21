from pong_repository import PongRepository 
import json
from exception import InvalidUsage

EMPTY_GUID = '00000000-0000-0000-0000-000000000000'
PLAYER_ID = 'playerId'
TIME_FINISHED = 'timeFinished'

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
            id1 = EMPTY_GUID
        if 'playerId' in player2:
            id2 = player2['playerId']
        else:
            id2 = EMPTY_GUID
        return self.pong_repo.create_new_game(id1, id2)

    def get_game(self, game_id):
        return self.pong_repo.get_game(game_id)

    def update_game(self, game_id, body):
        player1 = body['player1']
        player2 = body['player2']
        if PLAYER_ID not in player1:
            raise InvalidUsage(f'The {PLAYER_ID} not found in player1', status_code=400)
        if PLAYER_ID not in player2:
            raise InvalidUsage(f'The {PLAYER_ID} not found in player2', status_code=400)
        game = self.pong_repo.get_game(game_id)
        print (game)
        if game is None:
            raise InvalidUsage('No game found', status_code=404)
        elif game[TIME_FINISHED] is not None:
            raise InvalidUsage('Game is finished', status_code=400)
        else:
            player1_game = game['player1']
            player2_game = game['player2']
            if player1_game[PLAYER_ID] == player1[PLAYER_ID] and player2_game[PLAYER_ID] == player2[PLAYER_ID]:
                self.pong_repo.update_game(game_id, player1, player2)
            elif player2_game[PLAYER_ID] == player1[PLAYER_ID] and player1_game[PLAYER_ID] == player2[PLAYER_ID]:
                self.pong_repo.update_game(game_id, player2, player1)
            else:
                InvalidUsage(f'PlayerIds did not match game', status_code=400)

            
            



from pong_repository import PongRepository


class PongService():
    def __init__(self):
        self.pong_repo = PongRepository()

    def get_player(self, id):
        return self.pong_repo.get_player(id)

    def create_player(self, id):
        return self.pong_repo.create_player(id)

    def get_players(self):
        return PongRepository.get_players()

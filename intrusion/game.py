from .player import Player
from .cards import Card

class GameState:
    def add_deck(self) -> None:
        pass

    def add_player(self, name: str) -> None:
        print(f"{name} has joined the game.")
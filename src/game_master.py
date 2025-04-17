from src.player import Player
from src.card import CardDeck

class GameMaster:

    def __init__(self, nb_players):

        self.nb_players = nb_players
        self.nb_alive_players = nb_players

        self.players = []


    def distribute_cards
    
    def start_game(self):
        
        while self.nb_alive_players != 1:
            pass
from loguru import logger
import numpy as np
import random

from player import Player
from bot_player import  RandomBotPlayer
from card import CardDeck
from draw import BoardDrawer
from __init__ import war_characters, return_random_name


class GameMaster:

    def __init__(self):

        self.nb_players = 0 
        self.nb_bot_players = -1
        self.nb_alive_players = self.nb_players

        self.list_players = []


    
    
    def init_game(self):

        # Number of total players
        while self.nb_players > 8 or self.nb_players < 2: 
        
            logger.info("WELCOME TO THE GUERILLA GAME")
            logger.info("SELECT NUMBER OF PLAYERS: 2 - 8 ")
            try:
                self.nb_players = int(input())
            except ValueError:
                print("You must enter a valid number")

        self.nb_alive_players = self.nb_players

        # Number of bots 
        while self.nb_bot_players < 0 or self.nb_bot_players > self.nb_players :
            logger.info(f"SELECT THE NUMBER OF BOTS 0 - {self.nb_players}")
            try:
                self.nb_bot_players = int(input())
            except:
                ValueError("You must enter a valid number")

        #Prepare List of players
        self.list_players = []

        for i in range(self.nb_bot_players):
            self.list_players.append(RandomBotPlayer(f"Bot_{return_random_name(war_characters)}"))

        for i in range(self.nb_players - self.nb_bot_players):
            self.list_players.append(Player(return_random_name(war_characters)))

        #Players with fewer card values start
            
        lowest_cards_value = np.inf
        starting_player = None
            
        for i in range(self.nb_players):
            player = self.list_players[i]
            player_cards_value = player.hp + player.defense

            if player_cards_value < lowest_cards_value:
                starting_player = i
                lowest_cards_value = player_cards_value

        self.list_players = self.list_players[starting_player:] + self.list_players[:starting_player]
        BoardDrawer.draw_full_board(self.list_players)


    def _ask_action(self):
        logger.info("WHAT'S YOUR MOVE? 1 (ATTACK) | 2 (CHANGE DEFENSE) | 3 (CHARGE)")

        while True:
            try:
                action = int(input())
                if 1 <= action <= 3:
                    return action
                else:
                    logger.warning("YOU MUST CHOOSE A VALID OPTION: 1, 2, or 3")
            except ValueError:
                logger.warning("INVALID INPUT, ENTER A NUMBER 1-3")

    
    def _select_target(self, player, allow_self=False):

        if allow_self:
            valid_targets = [tmp_player for tmp_player in self.list_players]
        else:
            valid_targets = [tmp_player for tmp_player in self.list_players if tmp_player.name != player.name]

        logger.info("SELECT A PLAYER")
        logger.info([tmp_player.name for tmp_player in valid_targets])

        while True:
            choice = input().strip()
            for tmp_player in valid_targets:
                if tmp_player.name == choice:
                    return tmp_player
            logger.warning("Invalid player name, try again.")


    def _handle_attack(self, attacker, defender):
        attacker.attack(defender)

        if defender.hp <= 0:
            logger.info(f"{defender.name} HAS BEEN DEFEATED!")
            self.nb_alive_players -= 1
            self.list_players = [player for player in self.list_players if player.hp > 0]

    
    def _handle_charge(self, charger):
        charger.charge()


    def _handle_defense_change(self, changer, targeted_player):
        changer.change_defense(targeted_player)
    

    def play_game(self):

        while self.nb_alive_players > 1 :

            for player in self.list_players:
                logger.info(f"{player.name}'s TURN")

                ### Bot Logic
                if player.is_bot:
                    action, target =  player.decide_action(self.list_players)

                    if action == "attack":
                        self._handle_attack(player,target)

                    elif action == "change_defense":
                        self._handle_defense_change(player,target)
                    
                    else :
                        self._handle_charge(player)

                else:
                    ### Human Logic
                    if player.charged:

                        target = self._select_target(player, allow_self=False)
                        self._handle_attack(player,target)
                    else:
                        
                        action = self._ask_action()

                        if action == 3: # Charge
                            self._handle_charge()

                        elif action == 2 : #Change defense

                            target = self._select_target(player, allow_self=True)
                            self._handle_defense_change(player,target)

                        elif action == 1 :

                            target = self._select_target(player, allow_self=False)
                            self._handle_attack(player,target)

                        else:
                            logger.error("INVALID ACTION")

                BoardDrawer.draw_full_board(self.list_players)




        logger.info(f"CONGRATULATIONS ! {self.list_players[0].name} WON !!!!")




            




game = GameMaster()
game.init_game()
game.play_game()



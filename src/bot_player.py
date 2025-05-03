from player import Player
import random 
from card import CardDeck
from loguru import logger

class BotPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.is_bot = True

    def decide_action(self, list_of_players):
        raise NotImplementedError("Must implement in subclass")
    
    def cheat_death(self):
        raise NotImplementedError("Bots must override cheat_death()")
    


class RandomBotPlayer(BotPlayer):

    def decide_action(self, list_of_players):
        
        if self.charged:
            possible_targets = [target for target in list_of_players if self.name != target.name]
            target = random.choice(possible_targets)

            return 'attack',target
        

        action = random.choice(["attack", "change_defense", "charge"])

        if action == 'attack':
            possible_targets = [target for target in list_of_players if self.name != target.name]
            target = random.choice(possible_targets)
            return 'attack',target
        

        elif action == "change_defense":
            possible_targets = list_of_players  # including self
            target = random.choice(possible_targets)
            return "change_defense", target

        elif action == "charge":
            return "charge", None
        
        
    def cheat_death(self):
        
        shape_choice = ["spade","club","diamond","heart"]

        bot_choice = random.choice(shape_choice)
        logger.info(f"{self.name} GUESSED {bot_choice}")

        card = CardDeck.draw_card()
        logger.info(f"DRAWN CARD SHAPE : {card['shape']}")
        

        if bot_choice != card["shape"]:
            self.hp = -1
            logger.info(f"{self.name} FELL IN THE BATTLE")

            for card in self.hp_cards:
                CardDeck.return_card(card)

            CardDeck.return_card(self.defense_card)

        else: 
            logger.info(f"{self.name} CHEATED DEATH")
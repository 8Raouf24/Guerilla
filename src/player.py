from src.card import CardDeck
from loguru import logger

class Player:
    """
    Player class.
    A player can attack, charge, or change the defense 
    """
    def __init__(self,name) -> None:

        self.name = name
        self.cards = sorted([CardDeck.draw_card() for i in range(4)], key=lambda card: card['value'])


        self.defense_card = self.cards[0]
        self.defense = self.defense_card['value']


        self.hp_cards = self.cards[1:]
        self.hp = sum(card['value'] for card in self.hp_cards)

        self.charged = False
        self.charge_card = None

    
    def _remove_opponent_charge(self, opponent):
        """Helper function to remove opponent charge"""
        if opponent.charge_card:
            logger.info(f"{opponent.name} LOST THEIR CHARGE!")
            opponent.charged = False
            CardDeck.return_card(opponent.charge_card)
            opponent.charge_card = None

    
    def _apply_damage(self, opponent, damage):
        """Helper function for damage calculation and cards removal"""
        while damage > 0 and opponent.hp_cards:
            card = opponent.hp_cards[-1]
            value = card['value']
            remaining = value - damage

            CardDeck.return_card(opponent.hp_cards.pop())

            if remaining > 0:
                replacement = CardDeck.search_card(remaining)
                logger.info(f"Resting hp card given : {replacement}")
                opponent.hp_cards.append(replacement)
                opponent.hp_cards.sort(key=lambda card: card['value'])
                break
            else:
                damage -= value

    def attack(self,opponent_player):
        """Attack another player with a card"""
        attack_card = CardDeck.draw_card()

        logger.info(f"{self.name} IS ATTACKING {opponent_player.name} with {attack_card}")
        

        if self.charged:
            logger.info(f"AND : {self.charge_card} ")
            attack_points = attack_card["value"] + self.charge_card["value"]

            self.charged = False
            self.charge_card = None

        else:
            
            attack_points = attack_card["value"]
        
        if attack_points > opponent_player.defense :

            self._remove_opponent_charge(opponent_player)
            
            damage = attack_points -  opponent_player.defense
            logger.info(f"DAMAGE DEALT : {damage}")

            if damage >= opponent_player.hp:
                survived = opponent_player.cheat_death()
                
                return survived

            opponent_player.hp -= damage
            self._apply_damage(opponent_player, damage)
                    
            return 1
        
        else:
            logger.info("TOO WEAK !!!")


        # Return to the deck the cards that were used during the attack and the cards from the removed hp of the opponent


    def change_defense(self,player):
        """
        Change the defense of any player on the table, including self
        """
        old_defense = player.defense_card
        CardDeck.return_card(player.defense_card)
        player.defense_card = CardDeck.draw_card() 
        player.defense = player.defense_card['value']

        logger.info(f"{self.name} IS CHANGING THE DEFENSE OF {player.name} FROM {old_defense} TO {player.defense_card} ")

        # Return the old defense to the deck 

    def charge (self):
        """Charge a card for this turn. Empower the next attack"""
        logger.info(f"{self.name} IS CHARGING !")

        self.charged = True
        self.charge_card = CardDeck.draw_card()

    def cheat_death(self):
        """
        If the player dies, he has the possibility the cheat death by guessing the correct shape of the next card
        """
        player_reponse = input("Choose a shape : spade | heart | club | diamond \n")

        logger.info(f"{self.name} GUESSED {player_reponse}")

        card = CardDeck.draw_card()


        logger.info(f"DRAWN CARD SHAPE : {card['shape']}")
        

        if player_reponse != card["shape"]:
            self.hp = -1
            logger.info(f"{self.name} FELL IN THE BATTLE")

            for card in self.hp_cards:
                CardDeck.return_card(card)

            CardDeck.return_card(self.defense_card)

            return False

        else: 
            logger.info(f"{self.name} CHEATED DEATH")

            return True

    
            






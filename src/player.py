from src.card import CardDeck

class Player:
    """
    Player class.
    A player can attack, charge, or change the defense 
    """
    def __init__(self,name) -> None:

        self.name = name
        self.cards = sorted([CardDeck.draw_card() for i in range(4)])

        self.defense_card = self.cards[0]
        self.defense = self.defense_card['value']


        self.hp_cards = self.cards[1:]
        self.hp = sum(card['value'] for card in self.hp_cards)

        self.charged = False
        self.charge_card = None

    def charge (self,card):
        """Charge a card for this turn. Empower the next attack"""
        self.charged = True 

        self.charge = CardDeck.draw_card()


    def attack(self,opponent_player, card):
        """Attack another player with a card"""

        if self.charged:
            attack_points = card + self.charge[1]
            self.charged = False
            self.charge = None

        else:
            attack_points = CardDeck.draw_card()[1]
        
        if attack_points > opponent_player.defense :


            #We remove the charge
            if opponent_player.charged :
                opponent_player.charge_card = None

            damage = attack_points -  opponent_player.defense

            if damage > opponent_player.hp:
                self.cheat_death()

            opponent_player.hp -= damage

            while damage > 0 :


        # Return to the deck the cards that were used during the attack and the cards from the removed hp of the opponent


    def change_defense(self,player, card):
        """
        Change the defense of any player on the table, including self
        """

        CardDeck.return_card(player.defense_card)
        player.defense_card = CardDeck.draw_card() 
        player.defense = player.defense_card['value']

        # Return the old defense to the deck 

    def cheat_death(self):
        """
        If the player dies, he has the possibility the cheat death by guessing the correct shape of the next card
        """
        player_reponse = input("Choose a shape : spade | heart | club | diamond")

        card = CardDeck.draw_card()

        if player_reponse != card["shape"]:
            self.hp = -1

            for card in self.hp_cards:
                CardDeck.return_card(card)

            CardDeck.return_card(self.defense_card)
            





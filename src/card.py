import random
import itertools
from typing import List





class CardDeck():
    deck = []

    @classmethod
    def _init_deck(self) -> None:
        #Creating our deck of cards with shapes and values

        shapes = ['heart','spade','club','diamond']
        numbers = list(range(1,14))
        deck = list(itertools.product(shapes,numbers))

        #King of diamonds = 0 
        for i in range(len(deck)):
            if (deck[i][0] == "carreau" ) & (deck[i][1] == 13):
                deck[i] = ("carreau",0)


        deck = [{'shape': shape, 'value': value} for (shape, value) in deck]



        #Shuffling the deck
        random.shuffle(deck)
        print(deck)


    @classmethod
    def draw_card(self):
        """
        Draw a card from the top of the deck 
        """
        return self.deck.pop(0)
    
    @classmethod
    def return_card(self,card):
        """
        Return a card to the end of the deck
        """
        self.deck.append(card)


CardDeck()._init_deck()
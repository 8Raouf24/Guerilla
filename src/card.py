import random
import itertools
from typing import List





class CardDeck():
    
    shapes = ['heart','spade','club','diamond']
    numbers = list(range(1,14))
    deck = list(itertools.product(shapes,numbers))

    #King of diamonds = 0 
    for i in range(len(deck)):
        if (deck[i][0] == "diamond" ) & (deck[i][1] == 13):
            deck[i] = ("diamond",0)


    deck = [{'shape': shape, 'value': value} for (shape, value) in deck]
    #Shuffling the deck
    random.Random(24).shuffle(deck)




        
        


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

    @classmethod
    def search_card(self,value):
        """
        Return a card to the end of the deck
        """
        for i in range(len(self.deck)) :
            if self.deck[i]['value']==value:
                return self.deck.pop(i)
                


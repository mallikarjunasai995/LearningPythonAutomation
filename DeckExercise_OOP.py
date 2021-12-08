from random import shuffle
from typing import Counter


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = [Card(value,suit) for suit in suits for value in values]
        print(self.cards)

    def count(self):
         return len(self.cards)
        
    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("only Full deck can be shuffled")
        shuffle(self.cards)
        return self

    def __deal(self,num):
        count = self.count()
        actual = min(count,num)
        if count == 0:
            raise ValueError("all cards were dealt")

        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_hand(self):
        pass




class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return f"{self.value} of {self.suit}"


pekata = Card("diamond",13)
print(pekata)
mukkalu = Deck()
print(mukkalu)


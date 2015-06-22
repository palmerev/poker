#playingcards.py
from random import shuffle

SUITS = ['C','H','S','D'] # Clubs, Hearts, Spades, Diamonds
VALUES = ['2','3','4','5','6','7','8','9','T','J','Q','K','A'] # T -> 10
RANKS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

class Card(object):
    RANKS_BY_VALUE = {value:rank for value,rank in zip(VALUES, RANKS)}
    CARD_NAMES = [value + suit for value in VALUES for suit in SUITS]
    def __init__(self, s):
        """Takes a string s of length 2 (the value and suit of a card)."""
        self.value, self.suit = s.upper()
        self.name = s.upper()
        self.rank = Card.RANKS_BY_VALUE[self.value]

    def __str__(self):
        return "".join(["'", self.name, "'"])

    def __repr__(self):
        return "".join(["'", self.name, "'"])

    def __cmp__(self, other):
        return cmp(self.rank, other.rank)


class Deck(object):
    def __init__(self):
        self.cards = [Card(x) for x in Card.CARD_NAMES]
        self.card_count = len(self.cards)
        self.shuffle()

    def __str__(self):
        return str([x.name for x in self.cards])

    def __repr__(self):
        return str([x.name for x in self.cards])

    def shuffle(self):
        if self.card_count > 0:
            shuffle(self.cards) #uses random.shuffle()
        else:
            print "Deck is empty!"

    def draw(self, n=1):
        if n < 1:
            print "Can't draw less than one card!"
        drawn = []
        #print "card_count is:", self.card_count, "n is:", n
        if n > self.card_count:
            n = self.card_count
        for i in range(n):
            drawn.append(self.cards.pop())
            self.card_count -= 1
        return drawn

    def deal_hand(self, num_cards, hand):
        hand.cards.extend(self.draw(num_cards))

#playingcards.py
from random import shuffle

SUITS = ['C','H','S','D'] # Clubs, Hearts, Spades, Diamonds
VALUES = ['2','3','4','5','6','7','8','9','T','J','Q','K','A'] # T -> 10
RANKS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

class Card(object):
    RANKS_BY_VALUE = {value:rank for value,rank in zip(VALUES, RANKS)}
    CARDS = [value + suit for value in VALUES for suit in SUITS]
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

'''    def test():
        ace_spades = Card('AS')
        print "created 'AS'"
        print ("AS.value:", ace_spades.value, "AS.suit:", ace_spades.suit, "AS.rank:",
               ace_spades.rank, "AS.name:", ace_spades.name
        )
        print "Ace of Spades prints as:", ace_spades

        q_hearts = Card('QH')
        print "created 'QH'"
        print ("QH.value:", q_hearts.value, "QH.suit:", q_hearts.suit, "QH.rank:",
               q_hearts.rank, "QH.name:", q_hearts.name
        )

        q_clubs = Card('QC')
        print "created 'QC'"
        print ("QC.value:", q_clubs.value, "QC.suit:", q_clubs.suit, "QC.rank:",
               q_clubs.rank, "QC.name:", q_clubs.name
        )

        print "AS < QH:", ace_spades < q_hearts, "AS > QH:", ace_spades > q_hearts
        print "AS == QH", ace_spades == q_hearts
        print "QH == QC", q_hearts == q_clubs
'''

class Deck(object):
    def __init__(self):
        self.deck = [Card(x) for x in Card.CARDS]
        print "created 52 Card deck"
        self.card_count = len(self.deck)

    def __str__(self):
        return str([x.name for x in self.deck])

    def __repr__(self):
        return str([x.name for x in self.deck])

    def shuffle(self):
        if self.card_count > 0:
            random.shuffle(self.deck)
        else:
            print "Deck is empty!"

    def draw(self, n=1):
        if n < 1:
            print "Can't draw less than one card!"
        drawn = []
        if n > self.card_count:
            n = self.card_count
            for i in range(n):
                drawn.append(self.deck.pop())
                self.card_count -= 1
        return drawn

    def deal_hand(self, num_cards, hand_obj):
        hand_obj.hand.extend(self.draw(num_cards))

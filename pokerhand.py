# pokerhand.py
from collections import Counter
from operator import itemgetter
from playingcards import Deck, Card

class Hand(Deck):
    HANDS_BY_RANK = {
        "High Card": 0,
        "One Pair": 1,
        "Two Pair": 2,
        "Three of a Kind": 3,
        "Straight": 4,
        "Flush": 5,
        "Full House": 6,
        "Four of a Kind": 7,
        "Straight Flush": 8,
        "Royal Flush": 9
    }

    def __init__(self):
        self.cards = [] #will contain Card objects

    def __str__(self):
        return str(self.cards)

    def __cmp__(self, other):
        """Returns 1 if calling object (self) ranks higher than other,
        -1 if self ranks lower, or 0 if they have equal rank."""
        self_rank = HANDS_BY_RANK[hand_type(self)]
        other_rank = HANDS_BY_RANK[hand_type(other)]
        return cmp(self_rank, other_rank)

    @property
    def values(self):
        return [c.value for c in self.cards]

    @property
    def suits(self):
        return [c.suit for c in self.cards]

    def handtype(self):
        """returns the type of hand as a string"""
        pass

    def order_by_rank(self, rev=False):
        """Returns the hand with the cards arranged from lowest to highest.
        If rev=True, cards are arranged from highest to lowest."""
        pass

    def validate(self):
        """Returns the string 'valid' if the hand is a valid poker hand,
        otherwise it return an string specifying why the hand is invalid."""
        #TODO: should return True if valid, raise custom exceptions if not
        pass

    def has_duplicates(self):
        quantities = [x[1] for x in self.value_counter().values()]
        if max(quantities) == 1:
            return False
        return True
        
    def is_straight(self):
        """Returns True if the hand is a straight (a consecutive sequence of
        values) or False if not. The ace-through-5 straight is not included."""

    def is_flush(self):
        """Returns True if the hand is a flush (all cards have same suit),
        False if not."""
        pass

    def suit_counter(self):
        """Returns a Counter object mapping a suit to the number of cards with
        that suit (i.e. suit : number_of_cards)."""
        pass

    def value_counter(self):
        """Returns a Counter object mapping value to the number of cards with
        that value (i.e. value : number_of_cards)."""
        pass

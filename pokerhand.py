# pokerhand.py
from collections import Counter
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
        print "created empty Hand"

    def __str__(self):
        return str(self.cards)

    def __cmp__(self, other):
        """Returns 1 if calling object (self) ranks higher than other,
        -1 if self ranks lower, or 0 if they have equal rank."""
        self_rank = HANDS_BY_RANK[handtype(self)]
        other_rank = HANDS_BY_RANK[handtype(other)]
        return cmp(self_rank, other_rank)

    @property
    def values(self):
        return [c.value for c in self.cards]

    @property
    def suits(self):
        return [c.suit for c in self.cards]

    @property
    def ranks(self):
        return sorted([Card.RANKS_BY_VALUE[c.value] for c in self.cards])

    def handtype(self):
        """returns the type of hand as a string"""
        flush = self.is_flush()
        straight = self.is_straight()
        #quantity of each card value, from most to least common
        card_counts = [x[1] for x in self.value_counter().most_common()]
        ordered_values = [x[0] for x in self.order_by_rank()]

        if "".join(ordered_values) == "TJQKA":
            return "Royal Flush"
        elif straight and flush:
            return "Straight Flush"
        elif flush and not straight:
            return "Flush"
        elif straight and not flush:
            return "Straight"
        elif max(card_counts) == 4:
            return "Four of a Kind"
        elif card_counts[0] == 3 and card_counts[1] == 2:
            return "Full House"
        elif card_counts[0] == 3:
            return "Three of a Kind"
        elif card_counts[0] == 2 and card_counts[1] == 2:
            return "Two Pair"
        elif card_counts[0] == 2:
            return "One Pair"
        else:
            return "High Card"


    def order_by_rank(self, rev=False):
        """Returns the hand with the cards arranged from lowest to highest.
        If rev=True, cards are arranged from highest to lowest."""
        cards_with_ranks = [(playingcards.RANKS_BY_VALUE[c.value], c) for c in self.cards]
        cards_with_ranks.sort()
        if rev:
            return [c[1] for c in reversed(cards_with_ranks)]
        return [c[1] for c in  cards_with_ranks]


    def has_duplicates(self):
        quantities = [x[1] for x in self.value_counter().values()]
        if max(quantities) == 1:
            return False
        return True

    def is_straight(self):
        """Returns True if the hand is a straight (a consecutive sequence of
        values) or False if not. The ace-through-5 straight is not included."""
        if not self.has_duplicates():
            r = self.ranks
            if max(r) - min(r) == 4:
                return True
        return False

    def is_flush(self):
        """Returns True if the hand is a flush (all cards have same suit),
        False if not."""
        return len(self.suit_counter()) == 1

    def suit_counter(self):
        """Returns a Counter object mapping a suit to the number of cards with
        that suit (i.e. suit : number_of_cards)."""
        return Counter(self.suits)

    def value_counter(self):
        """Returns a Counter object mapping value to the number of cards with
        that value (i.e. value : number_of_cards)."""
        return Counter(self.values)

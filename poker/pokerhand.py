# pokerhand.py
from collections import Counter, namedtuple
from random import randint
import playingcards as pc

class Hand(pc.Deck):
    SERIES_HANDS = ["High Card", "Straight", "Flush", "Straight Flush", "Royal Flush"]
    GROUPED_HANDS = ["Four of a Kind", "Three of a Kind", "Full House", "Two Pair", "One Pair"]
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
        super(Hand, self).__init__()
        self.cards = [] #will contain Card objects

    def __str__(self):
        return " ".join([str(sorted(self.cards, reverse=True)), self.handtype()])

    def __cmp__(self, other):
        """Returns 1 if calling object (self) ranks higher than other,
        -1 if self ranks lower, or 0 if they have equal rank."""
        hand_rank1 = Hand.HANDS_BY_RANK[self.handtype()]
        hand_rank2 = Hand.HANDS_BY_RANK[other.handtype()]
        result = cmp(hand_rank1, hand_rank2)
        if result: #winner by hand rank
            return result
        #tiebreakers
        elif self.handtype() in Hand.SERIES_HANDS:
            return cmp(sorted(self.cards, reverse=True), sorted(other.cards, reverse=True))
        elif self.handtype() in Hand.GROUPED_HANDS:
            return self.break_grouped_hand_tie(other)
        else:
            raise ValueError, "unrecognized hand in Hand.__cmp__"

    def add(self, *card_names):
        self.cards.extend(pc.Card(name) for name in card_names)

    def break_grouped_hand_tie(self, other):
        cr_pairs1 = Hand.make_count_rank_pairs(self)
        cr_pairs2 = Hand.make_count_rank_pairs(other)
        #print "cr_pairs1:", cr_pairs1
        #print "cr_pairs2:", cr_pairs2
        return cmp(cr_pairs1, cr_pairs2)

    def make_count_rank_pairs(self):
        CRPair = namedtuple('CRPair', 'count rank')
        card_list = []
        #take value, count pairs from dictionary and make a list of count, rank pairs
        for val, cnt in self.value_counter().items():
            cr = CRPair(count=cnt ,rank=pc.Card.RANKS_BY_VALUE[val])
            card_list.append(cr)
        return sorted(card_list, reverse=True)

    @property
    def values(self):
        return [c.value for c in sorted(self.cards)]

    @property
    def suits(self):
        return [c.suit for c in self.cards]

    @property
    def ranks(self):
        return sorted(pc.Card.RANKS_BY_VALUE[c.value] for c in self.cards)

    def discard_all(self):
        del self.cards[:]

    def handtype(self):
        """returns the type of hand as a string"""
        flush = self.is_flush()
        straight = self.is_straight()
        #quantity of each card value, from most to least common
        card_counts = [x[1] for x in self.value_counter().most_common()]
        ordered_values = [c.value for c in sorted(self.cards, reverse=True)]

        if "".join(ordered_values) == "AKQJT" and flush:
            return "Royal Flush"
        elif (straight or "".join(ordered_values) == "A5432") and flush:
            return "Straight Flush"
        elif flush and not straight:
            return "Flush"
        elif (straight or "".join(ordered_values) == "A5432") and not flush:
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
        pass
        '''#TODO: remove this function and see if built-in sort works with __cmp__ overridden
        """Returns the hand with the cards arranged from lowest to highest.
        If rev=True, cards are arranged from highest to lowest."""
        cards_with_ranks = [(pc.Card.RANKS_BY_VALUE[c.value], c) for c in self.cards]
        cards_with_ranks.sort()
        if rev:
            return [c[1] for c in reversed(cards_with_ranks)]
        return [c[1] for c in cards_with_ranks]
        '''

    def has_duplicates(self):
        quantities = self.value_counter().values()
        if max(quantities) == 1:
            return False
        return True

    def is_straight(self):
        """Returns True if the hand is a straight (a consecutive sequence of
        values) or False if not. The ace-through-5 straight is not included."""
        if not self.has_duplicates():
            r = self.ranks
            if abs(max(r) - min(r)) == 4:
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

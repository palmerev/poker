#poker_hand.py
from collections import Counter
SUITS = ['C','H','S','D'] # Clubs, Hearts, Spades, Diamonds
VALUES = ['2','3','4','5','6','7','8','9','T','J','Q','K','A'] # T -> 10
RANKS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
RANKS_BY_VALUE = dict(zip(VALUES, RANKS))
CARDS = [y + x for x in SUITS for y in VALUES]

def tell_hand(hand):
    hand_is_valid = validate_hand(hand)
    if hand_is_valid != "True":
        return hand_is_valid
    else:
        flush = is_flush(hand)
        straight = is_straight(hand)
        card_counts = make_set_counts(hand)
        ordered_values = [x[0] for x in order_by_rank(hand)]

        if "".join(ordered_values) == "TJQKA":
            return "Royal Flush", ordered_values
        elif straight and flush:
            return "Straight Flush", ordered_values
        elif flush and not straight:
            return "Flush", ordered_values
        elif straight and not flush:
            return "Straight", ordered_values
        elif max(card_counts) == 4:
            return "Four of a Kind", ordered_values
        elif card_counts[0] == 3 and card_counts[1] == 2:
            return "Full House", ordered_values
        elif card_counts[0] == 3:
            return "Three of a Kind", ordered_values
        elif card_counts[0] == 2 and card_counts[1] == 2:
            return "Two Pair", ordered_values
        elif card_counts[0] == 2:
            return "One Pair", ordered_values
        else:
            return "High Card", ordered_values #return highest card

def validate_hand(hand):
    hand_set_size = len(set(hand))
    hand_size = len(hand)
    if hand_size != 5:
        return "wrong number of cards in hand"
    if hand_size != hand_set_size:
        return "duplicate card in hand"
    for card in hand:
        if card not in CARDS:
            return "invalid card in hand"
    return "True"

def order_by_rank(hand):
    ranks_in_hand = []
    for card in hand:
        ranks_in_hand.append((RANKS_BY_VALUE[card[0]], card))
    #print "hand_ranks", hand_ranks
    cards_with_ranks = sorted(ranks_in_hand)
    #print "cards_with_ranks", cards_with_ranks
    ordered_hand = [x[1] for x in cards_with_ranks]
    #print "ordered_hand", ordered_hand
    return ordered_hand

def is_straight(hand):
    in_order_hand = order_by_rank(hand)
    vals = [x[0] for x in in_order_hand]
    if "".join(vals) == "2345A":
        return True
    i = 0
    j = 4
    values_length = len(VALUES)
    #print "vals", vals
    while j < values_length:
        sequence = VALUES[i:j+1]
        #print "sequence", sequence
        if vals == sequence:
            return True
        i += 1
        j += 1
    return False

def make_suits(h):
    suits = [x[1] for x in h]
    suit_counts = Counter(suits)
    return suit_counts

def is_flush(h):
    by_suits = make_suits(h)
    suit_qty = by_suits.most_common()
    if suit_qty[0][1] == 5: #all 5 cards the same suit
        return True

def make_value_counts(h):
    vals = [x[0] for x in h]
    value_counts = Counter(vals)
    return value_counts

def group_by_kind(h):
    cards_by_rank = make_value_counts(h).most_common()
    counts_only = [x[1] for x in cards_by_rank]
    return counts_only

def test():
    RF = tell_hand(['AH', 'QH', 'KH', 'TH', 'JH'])
    print "Testing Royal Flush: %r, %r" % (RF, RF == "Royal Flush")
    SF = tell_hand(['KD', 'QD', 'JD', 'TD', '9D'])
    print "Testing Straight Flush: %r, %r" % (SF, SF == "Straight Flush")
    FK = tell_hand(['AD', 'AS', 'AC', 'AH', '2C'])
    print "Tesing Four of a Kind: %r, %r" % (FK, FK == "Four of a Kind")
    FH = tell_hand(['AD', 'AS', 'AC', '2D', '2S'])
    print "Testing Full House: %r, %r" % (FH, FH == "Full House")
    FL = tell_hand(['2C', '5C', '7C', '8C', 'AC'])
    print "Testing Flush: %r, %r" % (FL, FL == "Flush")
    ST = tell_hand(['2H','3S','4S', '5S','6S'])
    print "Testing Straight: %r, %r" % (ST, ST == "Straight")
    STLOW = tell_hand(['AH', '2D','3D' ,'4D' ,'5D'])
    print "Testing Straight, Ace Low: %r, %r" % (STLOW, STLOW == "Straight")
    THK = tell_hand(['AH', 'AD', 'AC', 'KH', 'QH'])
    print "Testing Three of a Kind: %r, %r" % (THK, THK == "Three of a Kind")
    TP = tell_hand(['AH', 'AD', 'KH', 'KD', 'QC'])
    print "Testing Two Pair: %r, %r" % (TP, TP == "Two Pair")
    OP = tell_hand(['AH', 'AD', 'KH', '2D', 'QC'])
    print "Testing One Pair: %r, %r" % (OP, OP == "One Pair")
    HC = tell_hand(['AH', '4D', 'KH', '2D', 'QC'])
    print "Testing High Card: %r" % (HC,)

if __name__ == '__main__':
    test()

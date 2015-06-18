#read_hands.py
import urllib
from poker_hand import *
poker_txt = urllib.urlopen(
            "https://projecteuler.net/project/resources/p054_poker.txt")
total1 = 0
total2 = 0
for line in poker_txt:
    line = line.strip()
    cards = line.split(" ")
    p1_cards = cards[:5]
    p2_cards = cards[5:]
    #if is_straight(p1_cards) and is_straight(p2_cards):
    #    print "two straights:", order_by_rank(p1_cards), order_by_rank(p2_cards)
    result = play_hands(p1_cards, p2_cards)

    if result == "Player 1 Wins":
        total1 += 1
    elif result == "Player 2 Wins":
        total2 += 1

poker_txt.close()

print "Player 1 wins", total1, "hands."
print "Player 2 wins", total2, "hands."

def test_read_hands():
    with open("test_read_hands3.txt", "w") as f:
        poker_txt = urllib.urlopen(
                    "https://projecteuler.net/project/resources/p054_poker.txt")
        total1 = 0
        total2 = 0
        for line in poker_txt:
            line = line.strip()
            cards = line.split(" ")
            p1_cards = cards[:5]
            p2_cards = cards[5:]
            hand_one = order_by_rank(p1_cards)
            hand_two = order_by_rank(p2_cards)
            #if is_straight(p1_cards) and is_straight(p2_cards):
            #    print "two straights:", order_by_rank(p1_cards), order_by_rank(p2_cards)
            outcome = play_hands(p1_cards, p2_cards)

            if outcome == "Player 1 Wins":
                total1 += 1
            elif outcome == "Player 2 Wins":
                total2 += 1
            result = " ".join([str(hand_one), str(hand_two), tell_hand(hand_one),
                tell_hand(hand_two), outcome, "\n"]
                )
            f.write(result)
        poker_txt.close()

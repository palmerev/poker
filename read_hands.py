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
    result = two_player_hand(p1_cards, p2_cards)

    if result == "Player 1 Wins":
        total1 += 1
    elif result == "Player 2 Wins":
        total2 += 1
        
poker_txt.close()

print "Player 1 wins", total1, "hands."
print "Player 2 wins", total2, "hands."

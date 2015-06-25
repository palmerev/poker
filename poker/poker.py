#poker.py
from pokergame import PokerGame
from int_validation import get_int

def make_player_list(num_players):
    """prompts the user to enter a name for each of n number of players,
     and returns them in a list"""
    player_names = []
    while len(player_names) < num_players:
            name = raw_input("Enter a name for player {0}: ".format(len(player_names) + 1))
            if name in player_names:
                print "There is already a player with that name."
                continue
            else:
                player_names.append(name)
    return player_names

print "Welcome to Five-Card Draw!"
while True:
    try:
        num_players = get_int("Enter a number of players from two to five: ")
        if num_players < 2 or num_players > 5:
            raise ValueError
        break
    except ValueError:
        print "Input must be an integer between two and five."
players = make_player_list(num_players)
print players
print "Dealing hands..."
game = PokerGame(*players)

game.play()

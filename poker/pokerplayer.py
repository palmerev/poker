#pokerplayer.py
from playingcards import *
from pokerhand import *
from pokergame import *

class Player(object):
    def __init__(self, name, chips=100):
        self.name = name
        #print "created Player", self.name
        self.hand = Hand()
        self.chips = chips
        self.has_played = False # updated each turn

    def __repr__(self):
        return self.name, self.hand, "chips:", self.chips

    def show_hand(self):
        print self.hand

    def bet(self, the_game, amount):
        if amount > self.chips:
            amount = self.chips
        self.chips -= amount
        the_game.pot += amount
        self.played = True

    def fold(self, the_game):
        the_game.players.remove(self)

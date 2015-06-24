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

    def check(self, the_game):
        for player in the_game.players:
            if player.has_played:
                raise BetValueError
        print self.name, "checks"
        self.has_played = True

    def bet(self, the_game, amount):
        if amount <= 0:
            print "bet amount must be positive"
            return
        if amount > self.chips:
            amount = self.chips
        self.chips -= amount
        the_game.pot += amount
        self.played = True

    def fold(self, the_game):
        the_game.players.remove(self)

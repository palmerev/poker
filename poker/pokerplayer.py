#pokerplayer.py
from playingcards import *
from pokerhand import *
from pokergame import *

class Player(object):
    def __init__(self, name, chips=100):
        self.name = name
        self.hand = Hand()
        self.chips = chips
        self.has_played = False # updated each turn
        self.has_folded = False

    def __repr__(self):
        return self.name, self.hand, "chips:", self.chips

    def __cmp__(self, other):
        return cmp(self.hand, other.hand)

    #def show_hand(self):
    #    print self.hand

    #def check(self, the_game):
    #    for player in the_game.players:
    #        if player.has_played:
    #            raise BetValueError
    #    print self.name, "checks"
    #    self.has_played = True

    def bet(self, the_game, amount):
        if amount <= 0:
            raise BetValueError("Bet value must be positive.")
        if amount < the_game.min_bet:
            raise BetValueError("You must bet at least {0} chips.".format(the_game.min_bet))
        if amount > self.chips:
            amount = self.chips
        self.chips -= amount
        the_game.pot += amount
        the_game.min_bet = amount
        self.has_played = True

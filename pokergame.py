#pokergame.py
import playingcards as pcards #Card, Deck
import pokerhand as phand

class PokerGame(object):
    def __init__(self, *players):
        self.players = [Player(p) for p in players]
        self.deck = pcards.Deck()
        self.pot = 0

    def __str__(self):
        pass

    def add_players(self, *p):
        self.players.extend(p)

    def remove_player(self, p):
        self.players.remove(p)

    def play(self):
        pass

class Player(object):
    def __init__(self, name, chips=100):
        self.name = name
        print "created Player", self.name
        self.hand = pcards.Hand()
        self.chips = chips

    def __str__(self):
        return self.name, self.hand

    def __cmp__(self):
        pass

    def show_hand(self):
        print self.hand

    def bet(self, num_chips):
        if num_chips > self.chips:
            num_chips = self.chips

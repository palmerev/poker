#pokergame.py
from playingcards import * #Card, Deck
from pokerhand import *

class PokerGame(object):
    def __init__(self, *players):
        self.players = [Player(p) for p in players]
        self.deck = Deck()
        self.pot = 0

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def add_players(self, p):
        self.players.append(p)

    def remove_player(self, p):
        self.players.remove(p)

    def show_game_menu(self, p):
        pass

    def play(self):
        for player in self.players:
            self.deck.deal_hand(player, 5)
            assert(len(player.hand) == 5))
        for player in self.players:
            self.show_game_menu(player)

    def end_turn(self):
        for player in self.players:
            if player.has_played:
                player.has_played = False
        self.deck.reset()

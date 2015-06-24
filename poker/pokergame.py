#pokergame.py
from playingcards import * #Card, Deck
from pokerhand import *
from pokerplayer import *
from int_validation import *

class BetValueError(object):
    def __init__(self, message=None):
        if message is not None:
            self.message = message

    def __str__(self):
        return repr(self.message)

class TurnError(object):
    def __init__(self, message=None):
        if message is not None:
            self.message = message

    def __str__(self):
        return repr(self.message)

class PokerGame(object):
    def __init__(self, *players):
        self.players = [Player(p) for p in players]
        self.deck = Deck()
        self.pot = 0
        self.min_bet = 0

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def add_players(self, p):
        self.players.append(p)

    def remove_player(self, p):
        self.players.remove(p)

    def main_turn_menu(self, p, options):
        done = False
        has_bet = False
        while not done:
            print "********************************"
            print "{0}, it's your turn. You may:".format(p.name)
            i = 0
            options_iter = iter(options)
            for option in options_iter:
                #skip over 'bet' if they've already made a bet this turn
                if has_bet and option == "bet":
                    option = next(options)
                    i += 1
                else:
                    i += 1
                print "{0}) {1}".format(i, option)
            while True:
                try:
                    selection = get_int("CHOOSE AN OPTION: ")
                    if selection < 1 or selection > len(options):
                        raise ValueError
                    elif has_bet and selection == options.index("bet"):
                        raise BetValueError("You've already made a bet this turn.")
                    break
                except ValueError:
                    print "Choice must be between {0} and {1}.".format(1, len(options))
                except BetValueError as e:
                    print e.message
        return selection

    def play(self):
        actions = ["see hand and chips", "bet", "fold", "end turn"]
        for player in self.players:
            self.deck.deal_hand(5, player.hand)
            assert(len(player.hand) == 5)
        for player in self.players:
            end_turn = False
            while not end_turn:
                choice = self.main_turn_menu(player, actions)
        try:
            self.end_hand()
        except TurnError as e:
            print e.message

    def end_hand(self):
        for player in self.players:
            if player.has_played:
                player.has_played = False
            else:
                raise TurnError("Not all players have played")
        self.deck.reset()

#pokergame.py
from playingcards import SUITS, VALUES, RANKS
from playingcards import Card
from playingcards import Deck
from pokerhand import Hand
from int_validation import get_int

def clear_screen():
    print '\n' * 50

class BetValueError(Exception):
    def __init__(self, message=None):
        if message is not None:
            self.message = message

    def __str__(self):
        return repr(self.message)

class TurnError(Exception):
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
        self.has_active_players = True
    def __str__(self):
        pass

    def __repr__(self):
        pass

    def add_players(self, p):
        self.players.append(p)

    def remove_player(self, p):
        self.players.remove(p)

    def main_turn_menu(self, player, options):
        has_bet = False
        print "********************************"
        print "{0}, it's your turn. You may:".format(player.name)
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
                option_num = get_int("CHOOSE AN OPTION: ")
                if option_num < 1 or option_num > len(options):
                    raise ValueError
                elif has_bet and option_num == options.index("bet"):
                    raise BetValueError("You've already made a bet this turn.")
                break
            except ValueError:
                print "Choice must be between {0} and {1}.".format(1, len(options))
            except BetValueError as e:
                print e.message
        return options[option_num - 1]

    def player_status_menu(self, player):
        print "********************************"
        print "{0}:".format(player.name)
        print "hand:", player.hand
        print "chips:", player.chips
        raw_input("Press Enter to return to the main menu.")
        clear_screen()

    def bet_menu(self, player):
        print "********************************"
        print "{0}:".format(player.name)
        print "hand:", player.hand
        print "chips:", player.chips
        while True:
            bet_amt = get_int("Bet how much? (minimum is {0}) ".format(self.min_bet))
            try:
                player.bet(self, bet_amt)
                break
            except BetValueError as e:
                print e.message
        clear_screen()

    def discard_old_cards(self, player):
        player_card_names = [card.name for card in player.hand.cards]
        while True:
            discards = raw_input(" ")
            if discards == "":
                return
            discards_list = discards.split()
            for card_abbr in discards_list:
                if card_abbr.upper() not in Card.CARD_NAMES:
                    print "{0} is not a valid card.".format(i)
                    break
                if card_abbr.upper() not in player_card_names:
                    print "{0} is not a card in your hand!".format(c)
                    break
            else: #no break, cards all valid
                for i in discards_list:
                    c = Card(i)
                    player.hand.cards.remove(c)
                    print "discarded {0}.".format(c)
        raw_input("Press Enter to continue")
        player.has_played = True

    def get_new_cards(self, player):
        print "{0}, your hand is: {1}".format(player.name, player.hand)
        print "If you'd like to get some new cards, enter their abbreviations, separated by spaces."
        print "Otherwise, press Enter."
        self.discard_old_cards(player);
        num_cards = len(player.hand)
        if num_cards < 5:
            num_discarded = 5 - num_cards
            self.deck.deal_hand(num_discarded, player.hand);
        print "Your new hand is: {0}".format(player.hand)
        raw_input("Press Enter to continue")

    def betting_round(self):
        turn_actions = [
            "see hand and chips",
            "bet",
            "fold",
            # "end turn"
        ]
        for player in self.players:
            player.has_played = False
            while not player.has_played:
                choice = self.main_turn_menu(player, turn_actions)
                if choice == "see hand and chips":
                    self.player_status_menu(player)
                elif choice == "bet":
                    self.bet_menu(player)
                elif choice == "fold":
                    confirm_fold = ""
                    while not (confirm_fold == 'y' or confirm_fold == 'n'):
                        confirm_fold = raw_input("Are you sure? (y/n)")
                        if confirm_fold.lower() == 'y':
                            player.has_played = True
                            player.folded = True
                # elif choice == "end turn":
                #     print "{0}, your turn is over.".format(player.name)
                #     player.has_played = True
                else:
                    raise TurnError("main_turn_menu returned invalid choice.")
        self.min_bet = 0

    def score(self):
        for player in self.players:
            if not player.has_folded:
                print "{0} hand: {1}".format(player.name, player.hand)
        self.players.sort(reverse=True)
        if self.players[0] == self.players[1]:
            top_player1 = self.players[0]
            top_player2 = self.players[1]
            print "split pot between {0} and {1}".format(top_player1.name, top_player2.name)
            print "{0}'s chips: {1}\t{2}'s chips: {3}".format(
                top_player1.name, top_player1.chips, top_player2.name, top_player2.chips
            )
        else:
            winner = self.players[0]
            print "{0} wins this hand with {1}".format(winner.name, winner.hand)
            winner.chips += self.pot
        self.pot = 0

    def end_hand(self):
        print "ending hand..."
        for player in self.players:
            player.has_folded = False
            if player.has_played:
                player.has_played = False

            else:
                raise TurnError("Not all players have played")
        self.min_bet = 0

    def play(self):
        for player in self.players:
            self.deck.deal_hand(5, player.hand)
            assert(len(player.hand) == 5)
            # initial round of betting
        self.betting_round()
        # optional exchange of cards
        for player in self.players:
            if not player.has_folded:
                self.get_new_cards(player)

        self.betting_round()
        self.score()
        try:
            self.end_hand()
        except TurnError as e:
            print e.message

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
        if amount < 0:
            raise BetValueError("Bet value must be positive.")
        if amount < the_game.min_bet:
            raise BetValueError("You must bet at least {0} chips.".format(the_game.min_bet))
        if amount > self.chips:
            raise BetValueError("You don't have that many chips.")
        self.chips -= amount
        the_game.pot += amount
        the_game.min_bet = amount
        self.has_played = True

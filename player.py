from wheel import Wheel
from table import Table
from bin_builder import BinBuilder
from bet import Bet
import sys


class Player(object):
    """Base class for players."""

    def __init__(self, table):
        self.stake = None
        self.rounds_to_go = sys.maxint
        self.table = table

    # PUBLIC
    def get_table(self):
        return self.table

    def get_stake(self):
        return self.stake

    def set_stake(self, budget):
        """Set the budget of the player."""
        self.stake = budget

    def set_rounds_to_go(self, rounds_to_go):
        """Set maximum rounds the player will play."""
        self.rounds_to_go = rounds_to_go

    def playing(self):
        """Returns true while the player is still active."""
        return self.rounds_to_go > 0 and self.stake > 0

    def place_bets(self, bets):
        """Updates the Table with the various Bet s.

        Args:
            bets: List of bets to be placed on the table. It could be just one
            bet

        Returns:
            True if all bets were placed ok.
            False if some bets couldn't be placed because run out of stake.
        """

        # if only one bet is passed, put it into a list
        if type(bets) != list:
            bets = [bets]

        # place each bet of the list
        for bet in bets:

            # check if player has money to bet
            if bet.get_amount() <= self.stake:

                # place bet on table
                self.table.place_bet(bet)

                # update stake and rounds to go
                self.stake -= bet.get_amount()
                self.rounds_to_go -= 1

            else:
                return False

        return True

    def win(self, bet):
        """Notification from the Game that the Bet was a winner.

        The amount of money won is available via a the winAmount() method
        of the Bet.

        Args:
            bet: The bet which won.
        """
        # update stake
        self.stake += bet.win_amount()

        # remove bet
        self.table.remove_bet(bet)

    def lose(self, bet):
        """Notification from the Game that the Bet was a loser.

        Args:
            bet: The bet wich lose."""

        # remove bet
        self.table.remove_bet(bet)

    def get_outcome(self, outcome_name):
        """Query a constructed wheel for getting outcome."""

        # create Whell
        wheel = Wheel()

        return wheel.get_outcome(outcome_name)


class Martingale(Player):
    """Martingale is a Player who places bets in Roulette.

    This player doubles their bet on every loss and resets their bet to a base
    amount on each win."""

    # DATA
    BASE_BET = "Black"
    BASE_AMOUNT = 1

    # FIELDS
    loss_count = 0
    bet_multiple = 1

    # PUBLIC
    def place_bets(self):
        """Create bet and update table with it."""

        # create bet
        bet = Bet(self.BASE_AMOUNT * self.bet_multiple,
                  self.get_outcome(self.BASE_BET))

        # update table with bet
        success = super(Martingale, self).place_bets(bet)

        # if bet coudn't be placed because no more money, leave and reset
        if not success:
            self.set_rounds_to_go(0)
            self.loss_count = 0
            self.bet_multiple = 1

    def win(self, bet):
        """Notification from the Game that the Bet was a winner.

        Reset loss_count and bet_multiple and update stake.

        Args:
            bet: The bet which won.
        """

        # reset loss_count and bet_multiple
        self.loss_count = 0
        self.bet_multiple = 1

        # update stake and remove bet from table
        super(Martingale, self).win(bet)

    def lose(self, bet):
        """Notification from the Game that the Bet was a loser.

        Update loss_count, bet_multiple and stake.

        Args:
            bet: The bet wich lose."""

        # update loss_count and bet_multiple
        self.loss_count += 1
        self.bet_multiple = self.bet_multiple * 2

        # update stake and remove bet from table
        super(Martingale, self).lose(bet)


class Passenger57(Player):
    """Stub subclass to get a player running in order to create Game class.

    The Passenger57 only bets a fixed amount to black outcome."""

    # DATA
    BASE_BET = "Black"
    BASE_AMOUNT = 100

    # FIELDS
    stake = 200

    # PUBLIC
    def place_bets(self):
        """Updates the Table with the various bets."""

        # create bet
        bet = Bet(self.BASE_AMOUNT, self.get_outcome(self.BASE_BET))

        # update table with bet
        super(Passenger57, self).place_bets(bet)

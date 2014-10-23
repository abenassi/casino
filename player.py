from wheel import Wheel
from table import Table
from bin_builder import BinBuilder
from bet import Bet


class Passenger57():

    """Stub class to get a player running in order to create Game class.

    The Passenger57 only bets a fixed amount to black outcome."""

    def __init__(self, table):
        self.black = self._get_black_outcome()
        self.table = table
        self.stake = 200

    # PUBLIC
    def place_bets(self):
        """Updates the Table with the various bets."""

        bet_amount = 100

        # check if player has money to bet
        if bet_amount <= self.stake:

            # create bet
            bet = Bet(100, self.black)

            # place bet on table
            self.table.place_bet(bet)

            # update stake
            self.stake -= bet.get_amount()

        else:
            return None

    def win(self, bet):
        """Notification from the Game that the Bet was a winner.

        The amount of money won is available via a the winAmount() method
        of the Bet.

        Args:
            bet: The bet which won.
        """

        # update stake
        self.stake += bet.win_amount()

        # clean table
        self.table.clean_table()

    def lose(self, bet):
        """Notification from the Game that the Bet was a loser.

        Args:
            bet: The bet wich lose."""

        # clean table
        self.table.clean_table()

    def get_table(self):
        return self.table

    def get_stake(self):
        return self.stake

    def set_stake(self, stake):
        self.stake = stake

    # PRIVATE
    def _get_black_outcome(self):
        """Query a constructed wheel for getting Black outcome."""

        # create Whell and BinBuilder instances
        wheel = Wheel()
        bb = BinBuilder()

        # build bins of the wheel with outcomes
        bb.build_bins(wheel)

        return wheel.get_outcome("Black")

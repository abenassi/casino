import unittest
from table import Table, InvalidBet
from bet import Bet
from outcome import Outcome
from roulette_game import RouletteGame


class TableTestCase(unittest.TestCase):
    """Test Table class methods."""

    def setUp(self):

        # create table
        self.table = Table()
        self.table.limit = 1000

        # create outcomes
        self.outcome_five = Outcome("00-0-1-2-3", RouletteGame.FiveBet)
        self.outcome_zero = Outcome("Number 0", RouletteGame.StraightBet)

        # create bets
        self.bet_five = Bet(100, self.outcome_five)
        self.bet_zero = Bet(100, self.outcome_zero)
        self.bet_zero_big = Bet(1100, self.outcome_zero)

    def test_is_valid(self):
        """Test is_valid method."""

        # check valid bets
        self.assertTrue(self.table.is_valid(self.bet_five))
        self.assertTrue(self.table.is_valid(self.bet_zero))

        # check invalid bet
        self.assertFalse(self.table.is_valid(self.bet_zero_big))

    def test_place_bet(self):
        """Test place_bet method."""

        # place valid bet
        self.table.place_bet(self.bet_five)

        # check is in bets list
        self.assertIn(self.bet_five, self.table.bets)

        # attempt to place invalid bet
        self.assertRaises(InvalidBet, self.table.place_bet, self.bet_zero_big)


def main():
    unittest.main()

if __name__ == '__main__':
    main()

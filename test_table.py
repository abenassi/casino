import unittest
from table import Table
from bet import Bet


class TableTestCase(unittest.TestCase):

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

    def test_is_valid(self):
        pass

    def test_place_bet(self):
        pass


def main():
    unittest.main()

if __name__ == '__main__':
    main()

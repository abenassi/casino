import unittest
from outcome import Outcome
from bin import Bin
from roulette_game import RouletteGame
from bet import Bet


class BetTestCase(unittest.TestCase):

    def setUp(self):
        self.outcome_five = Outcome("00-0-1-2-3", RouletteGame.FiveBet)
        self.outcome_zero = Outcome("Number 0", RouletteGame.StraightBet)
        self.bet_five = Bet(1000, self.outcome_five)
        self.bet_zero = Bet(1000, self.outcome_zero)

    def test_win_amount(self):
        self.assertEqual(self.bet_five.win_amount(), 1000 + 1000 * 6)
        self.assertEqual(self.bet_zero.win_amount(), 1000 + 1000 * 35)

    def test_lose_amount(self):
        self.assertEqual(self.bet_five.lose_amount(), 1000)
        self.assertEqual(self.bet_zero.lose_amount(), 1000)


def main():
    unittest.main()

if __name__ == '__main__':
    main()

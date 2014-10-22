import unittest
from outcome import Outcome
from bin import Bin
from roulette_game import RouletteGame


class TestBin(unittest.TestCase):

    def setUp(self):
        self.outcome_five = Outcome("00-0-1-2-3", 6)
        self.outcome_zero = Outcome("Number 0", 35)
        self.outcome_zerozero = Outcome("Number 00", 35)

        self.bin_zero = Bin(self.outcome_zero, self.outcome_five)
        self.bin_zerozero = Bin(self.outcome_zerozero, self.outcome_five)

        self.bin_zero2 = Bin()

    def test_contain_outcome(self):
        self.assertIn(Outcome("Number 0", RouletteGame.StraightBet),
                      self.bin_zero)

    def test_not_contain_outcome(self):
        self.assertNotIn(Outcome("Number 00", RouletteGame.StraightBet),
                         self.bin_zero)

    def test_contain_all_outcomes(self):
        self.assertIn(Outcome("Number 0", RouletteGame.StraightBet),
                      self.bin_zero)
        self.assertIn(Outcome("00-0-1-2-3", 6), self.bin_zero)

    def test_add(self):
        self.bin_zero2.add(self.outcome_zero)
        self.bin_zero2.add(self.outcome_five)
        self.assertIn(self.outcome_zero, self.bin_zero2)
        self.assertIn(self.outcome_five, self.bin_zero2)

    def test_print(self):
        self.assertEqual(str(self.bin_zero),
                         "Number 0 (35:1), 00-0-1-2-3 (6:1)")


def main():
    unittest.main()

if __name__ == '__main__':
    main()

import unittest
from outcome import Outcome
from wheel import Wheel
from non_random import NonRandom
from bin_builder import BinBuilder
from roulette_game import RouletteGame


class TestWheelConstruction(unittest.TestCase):

    def setUp(self):

        # create outcomes
        self.outcome_five = Outcome("00-0-1-2-3", 6)
        self.outcome_zero = Outcome("0", 35)
        self.outcome_zerozero = Outcome("00", 35)

        # create wheel and bin builder
        self.wheel = Wheel()
        self.bin_builder = BinBuilder()

    def test_add_outcome(self):
        """Testing add outcome to a Bin in a new Wheel."""

        # outcomes in Bin 0
        self.wheel.add_outcome(0, self.outcome_zero)
        self.wheel.add_outcome(0, self.outcome_five)

        # outcomes in Bin 00
        self.wheel.add_outcome(37, self.outcome_zerozero)
        self.wheel.add_outcome(37, self.outcome_five)

        # assert that outcomes are in Bin 0
        self.assertIn(self.outcome_zero, self.wheel.get(0))
        self.assertIn(self.outcome_five, self.wheel.get(0))

        # assert that outcomes are in Bin 00
        self.assertIn(self.outcome_zerozero, self.wheel.get(37))
        self.assertIn(self.outcome_five, self.wheel.get(37))

    def test_bin_building(self):
        """Testing bin building of the wheel using BinBuilder."""

        # build bins of the wheel
        self.bin_builder.build_bins(self.wheel)

        # create outcomes of bin 1
        outcomes_bin1 = [Outcome("Street 1-2-3", RouletteGame.StreetBet),
                         Outcome("Number 1", RouletteGame.StraightBet),
                         Outcome("Line 1-2-3-4-5-6", RouletteGame.LineBet),
                         Outcome("Low", RouletteGame.EvenBet),
                         Outcome("Odd", RouletteGame.EvenBet),
                         Outcome("Red", RouletteGame.EvenBet),
                         Outcome("Corner 1-2-4-5", RouletteGame.CornerBet),
                         Outcome("Dozen 1", RouletteGame.DozenBet),
                         Outcome("Column 1", RouletteGame.ColumnBet),
                         Outcome("Split 1-2", RouletteGame.SplitBet),
                         Outcome("Split 1-4", RouletteGame.SplitBet),
                         Outcome("00-0-1-2-3", RouletteGame.FiveBet)
                         ]

        # create outcomes of bin 2
        outcomes_bin2 = [Outcome("Number 00", RouletteGame.StraightBet),
                         Outcome("00-0-1-2-3", RouletteGame.FiveBet)]

        # check number of outcomes to be equal
        self.assertEqual(len(outcomes_bin1), len(self.wheel.get(1)))
        self.assertEqual(len(outcomes_bin2), len(self.wheel.get(37)))

        # check outcomes to be in the bin 1
        for outcome in outcomes_bin1:
            self.assertIn(outcome, self.wheel.get(1))

        # check outcomes to be in the bin 00
        for outcome in outcomes_bin2:
            self.assertIn(outcome, self.wheel.get(37))


class TestWheelAndNonRandomNumber(unittest.TestCase):

    def setUp(self):

        # create NonRandom instance with seed of 10
        nr = NonRandom()
        nr.set_seed(10)

        # create wheel with NonRandom instance
        self.wheel = Wheel(nr)

    def test_next(self):
        """Testing spinning the wheel to get next number."""

        self.assertEqual(self.wheel.next(), self.wheel.get(10))


def main():
    unittest.main()

if __name__ == '__main__':
    main()

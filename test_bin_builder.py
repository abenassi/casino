import unittest
from outcome import Outcome
from wheel import Wheel
from bin_builder import BinBuilder
from roulette_game import RouletteGame


class BaseTestCaseBinBuilder(unittest.TestCase):

    def setUp(self):
        self.wheel = Wheel()
        self.bin_builder = BinBuilder()


class GenStraightTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_straight(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Number 0", RouletteGame.StraightBet)
        self.outcome2 = Outcome("Number 16", RouletteGame.StraightBet)
        self.outcome3 = Outcome("Number 00", RouletteGame.StraightBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(0))
        self.assertIn(self.outcome2, self.wheel.get(16))
        self.assertIn(self.outcome3, self.wheel.get(37))


class GenSplitTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_split(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Split 1-2", RouletteGame.SplitBet)
        self.outcome2 = Outcome("Split 5-8", RouletteGame.SplitBet)
        self.outcome3 = Outcome("Split 35-36", RouletteGame.SplitBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(1))
        self.assertIn(self.outcome1, self.wheel.get(2))

        self.assertIn(self.outcome2, self.wheel.get(5))
        self.assertIn(self.outcome2, self.wheel.get(8))

        self.assertIn(self.outcome3, self.wheel.get(35))
        self.assertIn(self.outcome3, self.wheel.get(36))


class GenStreetTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_street(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Street 16-17-18", RouletteGame.StreetBet)
        self.outcome2 = Outcome("Street 1-2-3", RouletteGame.StreetBet)
        self.outcome3 = Outcome("Street 34-35-36", RouletteGame.StreetBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(16))
        self.assertIn(self.outcome1, self.wheel.get(17))
        self.assertIn(self.outcome1, self.wheel.get(18))

        self.assertIn(self.outcome2, self.wheel.get(1))
        self.assertIn(self.outcome2, self.wheel.get(2))
        self.assertIn(self.outcome2, self.wheel.get(3))

        self.assertIn(self.outcome3, self.wheel.get(34))
        self.assertIn(self.outcome3, self.wheel.get(35))
        self.assertIn(self.outcome3, self.wheel.get(36))


class GenCornerTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_corner(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Corner 1-2-4-5", RouletteGame.CornerBet)
        self.outcome2 = Outcome("Corner 2-3-5-6", RouletteGame.CornerBet)
        self.outcome3 = Outcome("Corner 32-33-35-36", RouletteGame.CornerBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(1))
        self.assertIn(self.outcome1, self.wheel.get(2))
        self.assertIn(self.outcome1, self.wheel.get(4))
        self.assertIn(self.outcome1, self.wheel.get(5))

        self.assertIn(self.outcome2, self.wheel.get(2))
        self.assertIn(self.outcome2, self.wheel.get(3))
        self.assertIn(self.outcome2, self.wheel.get(5))
        self.assertIn(self.outcome2, self.wheel.get(6))

        self.assertIn(self.outcome3, self.wheel.get(32))
        self.assertIn(self.outcome3, self.wheel.get(33))
        self.assertIn(self.outcome3, self.wheel.get(35))
        self.assertIn(self.outcome3, self.wheel.get(36))


class GenLineTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_line(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Line 1-2-3-4-5-6", RouletteGame.LineBet)
        self.outcome2 = Outcome("Line 31-32-33-34-35-36", RouletteGame.LineBet)
        self.outcome3 = Outcome("Line 10-11-12-13-14-15", RouletteGame.LineBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(1))
        self.assertIn(self.outcome1, self.wheel.get(2))
        self.assertIn(self.outcome1, self.wheel.get(3))
        self.assertIn(self.outcome1, self.wheel.get(4))
        self.assertIn(self.outcome1, self.wheel.get(5))
        self.assertIn(self.outcome1, self.wheel.get(6))

        self.assertIn(self.outcome2, self.wheel.get(31))
        self.assertIn(self.outcome2, self.wheel.get(34))
        self.assertIn(self.outcome2, self.wheel.get(36))

        self.assertIn(self.outcome3, self.wheel.get(11))
        self.assertIn(self.outcome3, self.wheel.get(13))
        self.assertIn(self.outcome3, self.wheel.get(14))


class GenDozenTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_dozen(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Dozen 1 to 12", RouletteGame.DozenBet)
        self.outcome2 = Outcome("Dozen 13 to 24", RouletteGame.DozenBet)
        self.outcome3 = Outcome("Dozen 25 to 36", RouletteGame.DozenBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(1))
        self.assertIn(self.outcome1, self.wheel.get(7))
        self.assertIn(self.outcome1, self.wheel.get(12))

        self.assertIn(self.outcome2, self.wheel.get(15))
        self.assertIn(self.outcome2, self.wheel.get(16))
        self.assertIn(self.outcome2, self.wheel.get(18))

        self.assertIn(self.outcome3, self.wheel.get(25))
        self.assertIn(self.outcome3, self.wheel.get(30))
        self.assertIn(self.outcome3, self.wheel.get(36))


class GenColumnTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_column(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Column 1", RouletteGame.ColumnBet)
        self.outcome2 = Outcome("Column 2", RouletteGame.ColumnBet)
        self.outcome3 = Outcome("Column 3", RouletteGame.ColumnBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(1))
        self.assertIn(self.outcome1, self.wheel.get(4))
        self.assertIn(self.outcome1, self.wheel.get(7))

        self.assertIn(self.outcome2, self.wheel.get(11))
        self.assertIn(self.outcome2, self.wheel.get(14))
        self.assertIn(self.outcome2, self.wheel.get(20))

        self.assertIn(self.outcome3, self.wheel.get(24))
        self.assertIn(self.outcome3, self.wheel.get(30))
        self.assertIn(self.outcome3, self.wheel.get(36))


class GenEvenTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_even(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Red", RouletteGame.EvenBet)
        self.outcome2 = Outcome("Odd", RouletteGame.EvenBet)
        self.outcome3 = Outcome("High", RouletteGame.EvenBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(3))
        self.assertIn(self.outcome1, self.wheel.get(23))
        self.assertIn(self.outcome1, self.wheel.get(34))

        self.assertIn(self.outcome2, self.wheel.get(1))
        self.assertIn(self.outcome2, self.wheel.get(17))
        self.assertIn(self.outcome2, self.wheel.get(35))

        self.assertIn(self.outcome3, self.wheel.get(19))
        self.assertIn(self.outcome3, self.wheel.get(31))
        self.assertIn(self.outcome3, self.wheel.get(36))


def main():
    unittest.main()

if __name__ == '__main__':
    main()

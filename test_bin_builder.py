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
        self.outcome1 = Outcome()
        self.outcome2 = Outcome()
        self.outcome3 = Outcome()

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(0))
        self.assertIn(self.outcome2, self.wheel.get(0))
        self.assertIn(self.outcome3, self.wheel.get(0))


class GenCornerTestCase(BaseTestCaseBinBuilder):
    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_corner(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome()
        self.outcome2 = Outcome()
        self.outcome3 = Outcome()

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(0))
        self.assertIn(self.outcome2, self.wheel.get(0))
        self.assertIn(self.outcome3, self.wheel.get(0))


class GenLineTestCase(BaseTestCaseBinBuilder):
    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_line(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome()
        self.outcome2 = Outcome()
        self.outcome3 = Outcome()

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(0))
        self.assertIn(self.outcome2, self.wheel.get(0))
        self.assertIn(self.outcome3, self.wheel.get(0))


class GenDozenTestCase(BaseTestCaseBinBuilder):
    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_dozen(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome()
        self.outcome2 = Outcome()
        self.outcome3 = Outcome()

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(0))
        self.assertIn(self.outcome2, self.wheel.get(0))
        self.assertIn(self.outcome3, self.wheel.get(0))


class GenColumnTestCase(BaseTestCaseBinBuilder):
    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_column(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome()
        self.outcome2 = Outcome()
        self.outcome3 = Outcome()

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(0))
        self.assertIn(self.outcome2, self.wheel.get(0))
        self.assertIn(self.outcome3, self.wheel.get(0))


class GenEvenTestCase(BaseTestCaseBinBuilder):
    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_even(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome()
        self.outcome2 = Outcome()
        self.outcome3 = Outcome()

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(0))
        self.assertIn(self.outcome2, self.wheel.get(0))
        self.assertIn(self.outcome3, self.wheel.get(0))


def main():
    unittest.main()

if __name__ == '__main__':
    main()

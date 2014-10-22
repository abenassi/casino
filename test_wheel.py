import unittest
from outcome import Outcome
from wheel import Wheel
from non_random import NonRandom


class TestWheelConstruction(unittest.TestCase):

    def setUp(self):

        # create outcomes
        self.outcome_five = Outcome("00-0-1-2-3", 6)
        self.outcome_zero = Outcome("0", 35)
        self.outcome_zerozero = Outcome("00", 35)

        # create wheel
        self.wheel = Wheel()

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

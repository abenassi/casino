import unittest
from outcome import Outcome


class TestOutcome(unittest.TestCase):

    def setUp(self):
        self.outcome1 = Outcome("1", 37)
        self.outcome2 = Outcome("1", 37)
        self.outcome3 = Outcome("2", 37)

    def test_equal(self):
        self.assertEqual(self.outcome1, self.outcome2)

    def test_unequal(self):
        self.assertNotEqual(self.outcome1, self.outcome3)

    def test_win_amount(self):
        self.assertEqual(self.outcome1.win_amount(10), 370)

    def test_print(self):
        self.assertEqual(str(self.outcome1), "1 (37:1)")

    def test_hash(self):
        self.assertEqual(hash(self.outcome1), hash(self.outcome2))


def main():
    unittest.main()

if __name__ == '__main__':
    main()

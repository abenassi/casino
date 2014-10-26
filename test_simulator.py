import unittest
from player import Martingale
from table import Table
from wheel import Wheel
from non_random import NonRandom
from game import Game
from simulator import Simulator


class SimulatorTestCase(unittest.TestCase):
    """Test Simulator class."""

    def setUp(self):

        # create NonRandom instance with seed
        nr = NonRandom()
        nr.set_seed(1)

        # create game and player
        wheel = Wheel(nr)
        table = Table()
        game = Game(wheel, table)
        player = Martingale(table)

        # assign default values to prevent future changes on them
        player.BASE_AMOUNT = 1
        player.BASE_BET = "Black"

        # create simulator instance
        self.simulator = Simulator(game, player)
        self.simulator.SAMPLES = 3

    def test_session(self):

        # execute one session
        stakes = self.simulator.session()

        # gather stats
        max_value = max(stakes)
        final_value = stakes[-1]
        duration = len(stakes)

        # check values derived from non-random generator
        self.assertEqual(max_value, 213)
        self.assertEqual(final_value, 213)
        self.assertEqual(duration, 250)

    def test_gather(self):

        # execute all sessions
        self.simulator.gather()

        # check gathered stats
        self.assertEqual(self.simulator.maxima, [213, 149, 223])
        self.assertEqual(self.simulator.final, [213, 22, 208])
        self.assertEqual(self.simulator.durations, [250, 105, 250])


def main():
    unittest.main()

if __name__ == '__main__':
    main()

import unittest
from wheel import Wheel
from player import Passenger57
from table import Table
from game import Game
from non_random import NonRandom


class GameTestCase(unittest.TestCase):
    """Test Game class for complete game cycle functioning.

    Uses a non_random number generator and a stub Player to predict wheel
    results and stake evolution based on a fixed sequence of winning bins."""

    def setUp(self):

        # create NonRandom instance with seed
        nr = NonRandom()
        nr.set_seed(1)

        # create game
        self.wheel = Wheel(nr)
        self.table = Table()
        self.game = Game(self.wheel, self.table)

        # create player
        self.player = Passenger57(self.table)
        self.player.set_stake(1000)

    # PUBLIC
    def test_cycle(self):
        """Test a cycle of the game, based on a non-random number generator."""

        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 900)

        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 800)

        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 900)

        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 800)

        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 700)

        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 800)

    def test_cycle_depleted_stake(self):
        """Test a cycle of the game, if player lose all its stake.

        Player should not be able to bet again if reaches the zero stake."""

        # reduce stake so player loses all and cannot bet again
        self.player.set_stake(300)

        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 200)

        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 100)

        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 200)

        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 100)

        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 0)

        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 0)


def main():
    unittest.main()

if __name__ == '__main__':
    main()

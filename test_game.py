from wheel import Wheel
from player import Passenger57
from table import Table
from game import Game


class TestGame():

    def __init__(self):
        self.wheel = Wheel()
        self.table = Table()
        self.player = Passenger57(self.table)
        self.player.set_stake(200)

    # PUBLIC
    def test_cycle(self):

        # creates game instance
        game = Game(self.wheel, self.table)

        # initial stake
        self._print_results()

        # cycle and print stake of player
        game.cycle(self.player)
        self._print_results()

        game.cycle(self.player)
        self._print_results()

        game.cycle(self.player)
        self._print_results()

        game.cycle(self.player)
        self._print_results()

        game.cycle(self.player)
        self._print_results()

        game.cycle(self.player)
        self._print_results()

    # PRIVATE
    def _print_results(self):
        print "Stake is: {}".format(self.player.get_stake())


def main():

    test = TestGame()
    test.test_cycle()

if __name__ == '__main__':
    main()

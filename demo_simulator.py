from player import Martingale
from table import Table
from wheel import Wheel
from non_random import NonRandom
from game import Game
from simulator import Simulator


def main():

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
    simulator = Simulator(game, player)
    simulator.SAMPLES = 3

    # execute simulator
    simulator.gather()

    # print results
    print "\n"
    print "Maxima", simulator.maxima, "\n"
    print "Final", simulator.final, "\n"
    print "Durations", simulator.durations, "\n"


if __name__ == '__main__':
    main()
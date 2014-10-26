from game import Game
from player import Martingale
from wheel import Wheel
from table import Table
from pprint import pprint


class Simulator():
    """Simulator execute Roulette simulation with a given Player placing bets.

    It reports raw statistics on a number of sessions of play."""

    INIT_DURATION = 250
    INIT_STAKE = 100
    SAMPLES = 100

    def __init__(self, game, player):
        self.game = game
        self.player = player
        self.maxima = []
        self.final = []
        self.durations = []

    # PUBLIC
    def session(self):
        """Executes a single game session.

        The Player is initialized with their initial stake and initial cycles
        to go. An empty List of stake values is created. The session loop
        executes until the Player playing() returns false. This loop executes
        the Game cycle(); then it gets the stake from the Player and appends
        this amount to the List of stake values. The List of individual stake
        values is returned as the result of the session of play.

        Returns:
            List of stake values."""

        stakes = []

        # init player
        self.player.set_rounds_to_go(self.INIT_DURATION)
        self.player.set_stake(self.INIT_STAKE)

        # cycle the game while player is active
        while self.player.playing():
            self.game.cycle(self.player)

            # append stake value to the list
            stakes.append(self.player.get_stake())

        return stakes

    def gather(self):
        """Executes the number of games sessions in samples.

        Each game session returns a List of stake values when the session is
        over (either the play reached their time limit or their stake was
        spent). Then the length, maximum value and final value in the session
        List are the resulting metrics gathered.

        These three metrics are appended to the durations, maxima and final
        lists.

        A client class will either display the raw metrics or produce
        statistical summaries."""

        for i in xrange(self.SAMPLES):

            print "Running session: " + str(i + 1)
            stakes = self.session()

            # extract metrics from stakes list
            max_value = max(stakes)
            final_value = stakes[-1]
            duration = len(stakes)

            # append to lists gathering metrics
            self.maxima.append(max_value)
            self.final.append(final_value)
            self.durations.append(duration)


def main():

    # create game and player
    wheel = Wheel()
    table = Table()
    game = Game(wheel, table)
    player = Martingale(table)

    # create simulator instance
    simulator = Simulator(game, player)
    simulator.gather()

    # print results
    print "Maxima", simulator.maxima, "\n"
    print "Final", simulator.final, "\n"
    print "Durations", simulator.durations, "\n"


if __name__ == '__main__':
    main()

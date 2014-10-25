class Game():

    """Game manages the sequence of actions that defines the game of Roulette.

    This includes notifying the Player to place bets, spinning the Wheel and
    resolving the Bets actually present on the Table."""

    def __init__(self, wheel, table):
        self.wheel = wheel
        self.table = table
        self.player = None

    # PUBLIC
    def cycle(self, player):
        """Execute a single cycle of play with a given Player.

        It will call thePlayers placeBets() method to get bets. It will call
        theWheels next() method to get the next winning Bin.

        It will then call theTables iterator to get an Iterator over the Bets.
        Stepping through this Iterator returns the individual Bet objects.

        If the winning Bin contains the Outcome, call the thePlayer win()
        method otherwise call the thePlayer lose() method.

        Args:
            player: A Player instance that places bets and get informed of
            winning and loses of them.
        """

        # place bets
        self.player = player
        self.player.place_bets()

        # spin the wheel
        win_bin = self.wheel.next()

        # iterate bets
        table = self.player.get_table()
        for bet in table:

            # check if bet is a winning one
            if bet.get_outcome() in win_bin:
                self.player.win(bet)

            else:
                self.player.lose(bet)

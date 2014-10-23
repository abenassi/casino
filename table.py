class InvalidBet(Exception):
    pass


class Table():
    """Table contains all the Bet s created by the Player.

    A table also has a betting limit, and the sum of all of a player’s bets
    must be less than or equal to this limit."""

    def __init__(self):

        self.limit = 1000
        self.bets = []

    def __iter__(self):
        pass

    def __str__(self):
        pass

    # PUBLIC
    def is_valid(self, bet):
        """Validates this bet.

        If the sum of all bets is less than or equal to the table limit, then
        the bet is valid, return true. Otherwise, return false.

        Args:
            bet: A Bet instance to be validated.
        """
        pass

    def place_bet(self, bet):
        """Adds this bet to the list of working bets.

        If the sum of all bets is greater than the table limit, then an
        exception should be thrown (Java) or raised (Python). This is a rare
        circumstance, and indicates a bug in the Player more than anything
        else.

        Args:
            bet: A Bet instance to be validated.
        Raises:
            InvalidBet
        """
        pass

class Bet():
    """Create a new Bet of a specific amount on a specific outcome."""

    def __init__(self, amount, outcome):

        self.amount_bet = amount
        self.outcome = outcome

    def __str__(self):
        return "{} on {}".format(self.amount_bet, self.outcome)

    def __repr__(self):
        return "{} on {}".format(self.amount_bet, self.outcome)

    # PUBLIC
    def win_amount(self):
        """Compute the amount won, given the amount of this bet."""
        return self.amount_bet + self.outcome.win_amount(self.amount_bet)

    def lose_amount(self):
        """Returns the amount bet as the amount lost."""
        return self.amount_bet

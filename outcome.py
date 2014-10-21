import hashlib


class Outcome():
    """Provide winning amount for a specific bet.

    Stores name and odds of a specific bet in a roulette and
    calculates winning amount for a specific bet amount on that
    outcome.

    Attributes:
        name: A string indicating the name of the bet.
        odds: The odds of the bet, indicating the multiplyer for
              the bet amount.
    """

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __str__(self):
        return "{} ({}:1)".format(self.name, self.odds)

    def __hash__(self):
        return int(hashlib.md5(self.name).hexdigest(), 16)

    # PUBLIC
    def win_amount(self, amount):
        """Returns winning amount for a bet amount placed."""
        return self.odds * amount

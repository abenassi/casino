class Outcome():

    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __str__(self):
        return "{} ({}:1)".format(self.name, self.odds)

    # PUBLIC
    def win_amount(self, amount):
        return self.odds * amount

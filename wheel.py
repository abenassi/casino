from bin import Bin
import random


class Wheel():

    def __init__(self, rng=None):
        self.bins = tuple(Bin() for i in xrange(38))
        self.rng = rng or random.Random()
        self.all_outcomes = {}

    # PUBLIC
    def add_outcome(self, number, outcome):
        """Add outcome to a specified bin.

        Args:
            number: Bin number (0 to 37).
            outcome: Outcome to be added to the Bin."""

        # add outcome to its bin
        self.bins[number].add(outcome)

        # add outcome to a dictionary
        self.all_outcomes[outcome.get_name()] = outcome

    def next(self):
        """Generates random number between 0 and 37, and returns that Bin."""

        return self.bins[self.rng.choice(xrange(38))]

    def get(self, number):
        """Returns the Bin of that number."""

        return self.bins[number]

    def get_outcome(self, name):
        """Returns a reference to an outcome mapped in the wheel."""

        # check if the outcome is mapped
        if name in self.all_outcomes:
            return self.all_outcomes[name]

        else:
            return None

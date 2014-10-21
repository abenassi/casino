from bin import Bin
import random


class Wheel():

    def __init__(self, rng=None):
        self.bins = tuple(Bin() for i in xrange(38))
        self.rng = rng or random.Random()

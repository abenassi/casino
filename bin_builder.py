from wheel import Wheel


class BinBuilder():
    """Build up Bins of a Wheel, filling them with its Outcomes.

    Calls one method for each kind of bet, that iterates through the Bins of
    the Wheel that have Outcomes on that bet and place those Outcomes in the
    Bin."""

    def __init__(self):
        self.bet_methods = (self._gen_straight, self._gen_split,
                            self._gen_street, self._gen_corner, self._gen_line,
                            self._gen_dozen, self._gen_column, self._gen_even)

    # PUBLIC
    def build_bins(self, wheel):
        """Fill Bins of a Wheel with Outcomes of each kind of bet."""

        # iterate all bet building methods
        for bet_method in self.bet_methods:
            bet_method(wheel)

    # PRIVATE
    def _gen_straight(self, wheel):
        print "OK"

    def _gen_split(self, wheel):
        print "OK"

    def _gen_street(self, wheel):
        print "OK"

    def _gen_corner(self, wheel):
        print "OK"

    def _gen_line(self, wheel):
        print "OK"

    def _gen_dozen(self, wheel):
        print "OK"

    def _gen_column(self, wheel):
        print "OK"

    def _gen_even(self, wheel):
        print "OK"


def quick_test():
    BinBuilder().build_bins(Wheel())

quick_test()

















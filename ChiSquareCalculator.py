import math


class ChiSquareCalculator:
    def __init__(self, expected_frequencies_, actual_frequencies_):
        self.expected = expected_frequencies_
        self.actual = actual_frequencies_

    @staticmethod
    def chi_square_sum(expected, actual):
        return pow((actual - expected), 2) / expected

    def calculate_chi_square(self):
        return math.fsum(
            [self.chi_square_sum(self.expected[i], self.actual[i]) for i in self.expected.keys()])

import math


class TheoreticalDistributionCalculator:
    def __init__(self, frequencies_, n_, average_, sd_, h_):
        self.n = n_
        self.average = average_
        self.sd = sd_
        self.h = h_
        self.frequencies = frequencies_

    @staticmethod
    def phi(u_):
        return 1 / math.sqrt(2 * math.pi) * math.exp(-1 * pow(u_, 2) / 2)

    def u(self, x_):
        return (x_ - self.average) / self.sd

    def expected_frequency(self, x_):
        return self.n * self.h * self.phi(self.u(x_)) / self.sd

    def calculate_expected_frequencies(self):
        frequencies_ = dict.fromkeys(self.frequencies.keys(), 0)
        for i in self.frequencies.keys():
            frequencies_[i] = self.expected_frequency(i)
        return frequencies_

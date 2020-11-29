import math


class SamplesToDistributionCalculator:
    samples = []
    frequencies = {}

    def __init__(self, samples_):
        self.samples = samples_
        self.n = len(samples_)

    def calculate_normal_distribution_parameters(self):
        self.frequencies = self.calculate_frequencies()
        average_ = self.calculate_average(self.n, self.frequencies)
        sd_ = self.calculate_sd(self.n, average_, self.frequencies)
        return average_, sd_

    def calculate_frequencies(self):
        frequencies_ = dict.fromkeys(self.samples, 0)
        for i in self.samples:
            frequencies_[i] += 1
        return frequencies_

    @staticmethod
    def calculate_average(n, frequencies_):
        return 1 / n * math.fsum([i * frequencies_[i] for i in list(frequencies_.keys())])

    @staticmethod
    def calculate_disperse(n, average_, frequencies_):
        return 1 / (n - 1) * math.fsum([pow(average_ - i, 2) * frequencies_[i] for i in list(frequencies_.keys())])

    def calculate_sd(self, n_, average_, frequencies_):
        return math.sqrt(self.calculate_disperse(n_, average_, frequencies_))

import math


class SamplePreprocessor:
    # in case the step h isn't defined by user or inappropriate, it will calculated according to Sturgis rule
    # otherwise it will passed forward
    def __init__(self, path_, degree_=-1):
        self.samples = self.get_samples_from_file(path_)
        self.degree = self.sturgis_rule(self.samples) if degree_ <= 0 else degree_
        self.h = (max(self.samples) - min(self.samples)) / self.degree
        self.samples = self.reduce_sample()

    @staticmethod
    def get_samples_from_file(path):
        samples_ = []
        for line in open(path):
            samples_ += [float(i) for i in line.replace(',', '.').split('\t')]
        return samples_

    @staticmethod
    def sturgis_rule(samples):
        return math.ceil(3.32 * math.log10(len(samples)) + 1)

    def reduce_sample(self):
        new_samples = []
        new_values = []
        for i in range(self.degree):
            new_values.append(min(self.samples) + (0.5 + i) * self.h)
        for i in self.samples:
            for j in new_values:
                if j - self.h / 2 <= i < j + self.h:
                    new_samples.append(j)
                    break
        return new_samples

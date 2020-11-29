class SamplePreprocessor:
    def __init__(self, path_, h_):
        self.samples = self.get_samples_from_file(path_)
        self.h = h_
        self.samples, self.degree = self.reduce_sample(self.samples)

    @staticmethod
    def get_samples_from_file(path):
        samples_ = []
        for line in open(path):
            samples_ += [float(i) for i in line.replace(',', '.').split('\t')]
        return samples_

    def reduce_sample(self, samples_):
        new_samples = []
        minimal = min(samples_)
        degree_ = 0
        while minimal <= max(samples_):
            for i in samples_:
                if minimal <= i < minimal + self.h:
                    new_samples.append(minimal)
            minimal += self.h
            degree_ += 1
        return new_samples, degree_

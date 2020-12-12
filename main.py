import SamplePreprocessor
import SamplesToDistributionCalculator
import TheoreticalDistributionCalculator
import ChiSquareCalculator
import IsNormalDistributionDefiner
import UserInterface
import math

import matplotlib.pyplot as plt


def main(significance, path, h=-1):
    preprocessor = SamplePreprocessor.SamplePreprocessor(path_=path, h_=h)
    samples, degree = preprocessor.samples, preprocessor.degree
    h = preprocessor.h  # redefine value in case we changed it inside preprocessor
    print('Degrees of freedom: ', degree)

    actual_calculator = SamplesToDistributionCalculator.SamplesToDistributionCalculator(samples)
    average, sd = actual_calculator.calculate_normal_distribution_parameters()
    print('Average: ', average)
    print('SD: ', sd)

    expected_calculator = \
        TheoreticalDistributionCalculator.TheoreticalDistributionCalculator(n_=actual_calculator.n,
                                                                            frequencies_=actual_calculator.frequencies,
                                                                            average_=average, sd_=sd, h_=h)
    expected_frequencies = expected_calculator.calculate_expected_frequencies()
    #
    chi_square_calculator = \
        ChiSquareCalculator.ChiSquareCalculator(actual_frequencies_=actual_calculator.frequencies,
                                                expected_frequencies_=expected_frequencies)
    chi_square = chi_square_calculator.calculate_chi_square()
    print('Chi_Square: ', chi_square)

    definer = IsNormalDistributionDefiner.IsNormalDistributionDefiner(degrees_=degree, significance_=significance)
    distribution = ""
    if definer.is_normal_distribution(chi_square):
        distribution = u"нормальное"
    else:
        distribution = "не нормальное"
    print(distribution)
    plt.hist(actual_calculator.samples)
    parts = path.split("/")
    plt.savefig(parts[len(parts) - 1].split(".")[0] + ".jpg")
    return [degree, round(average, 5), round(sd, 5), round(chi_square, 5), distribution]


def is_normal(significance, path, h=-1):
    preprocessor = SamplePreprocessor.SamplePreprocessor(path_=path, h_=h)
    samples, degree = preprocessor.samples, preprocessor.degree
    h = preprocessor.h

    actual_calculator = SamplesToDistributionCalculator.SamplesToDistributionCalculator(samples)
    average, sd = actual_calculator.calculate_normal_distribution_parameters()

    expected_calculator = \
        TheoreticalDistributionCalculator.TheoreticalDistributionCalculator(n_=actual_calculator.n,
                                                                            frequencies_=actual_calculator.frequencies,
                                                                            average_=average, sd_=sd, h_=h)
    expected_frequencies = expected_calculator.calculate_expected_frequencies()
    chi_square_calculator = \
        ChiSquareCalculator.ChiSquareCalculator(actual_frequencies_=actual_calculator.frequencies,
                                                expected_frequencies_=expected_frequencies)
    chi_square = chi_square_calculator.calculate_chi_square()

    definer = IsNormalDistributionDefiner.IsNormalDistributionDefiner(degrees_=degree, significance_=significance)
    return definer.is_normal_distribution(chi_square)


if __name__ == '__main__':
    significance_ = 0.05
    path_ = '/media/sf_virtualbox/Chi_v07c.txt'

    #  for i in range(1, 1000):
    #    if not is_normal(i / 1000, path_):
    #        print("limit significance for accepting as normal:", (i - 1) / 1000)
    #        break

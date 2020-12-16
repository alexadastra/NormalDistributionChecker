from scipy.stats import chi2


class IsNormalDistributionDefiner:
    def __init__(self, degrees_, significance_):
        self.critical = chi2.ppf(1 - significance_, degrees_ - 1)

    def is_normal_distribution(self, chi_square):
        return chi_square <= self.critical


if __name__ == '__main__':
    # print(chi2.ppf(0.995, 40))
    # print(chi2.ppf(.95, 8))
    pass

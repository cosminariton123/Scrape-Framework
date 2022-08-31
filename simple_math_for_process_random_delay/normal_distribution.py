import numpy as np


def normal_distribution_extraction(min, max):
    if min > max:
        raise ValueError("Minimum must be smaller than maximum")

    mean = (min + max) / 2
    distribution = (max - min) / 6

    generated = np.random.normal(mean, distribution)
    while generated < min or generated > max:
        generated = np.random.normal(mean, distribution)
    return generated
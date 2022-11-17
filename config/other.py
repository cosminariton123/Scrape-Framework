from simple_math_for_process_random_delay.normal_distribution import normal_distribution_extraction

from simple_math_for_process_random_delay.mathematical_constants import INF


INF = INF


NR_OF_PROCESSES = 10

#Iterator sifficiently large or fixed value(float or int, etc)
DELAY_BETWEEN_PROCESS_LAUNCHES = (normal_distribution_extraction(2, 7) for _ in range(10**10))


DELAY_BETWEEN_SEARCHES = 0


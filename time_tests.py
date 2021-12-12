import random
import math
import numpy as np
from tests.miller_rabin_test import *
from tests.trial_division_wheel_factorization import *
import timeit
import matplotlib.pyplot as plt

test_numbers = []

for i in range(2,20):
    rnd = random.random()
    rnd = math.ceil(rnd*pow(10,i))
    test_numbers.append(rnd)

miller_rabin_times = []
trial_division_wheel_factorization_times = []
for i in test_numbers:
    miller_rabin_times.append(float(timeit.timeit('miller_rabin(i)','from __main__ import miller_rabin,i')))
    trial_division_wheel_factorization_times.append(float(timeit.timeit('trial_division_wheel_factorization(i)','from __main__ import trial_division_wheel_factorization,i')))
    print(i)

plt.plot(test_numbers,miller_rabin_times,'b^')
plt.plot(test_numbers,trial_division_wheel_factorization_times,'g^')
plt.show()
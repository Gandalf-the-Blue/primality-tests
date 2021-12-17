import random
import math
import numpy as np
from tests.miller_rabin_test import *
from tests.trial_division_wheel_factorization import *
from tests.aks_test import *
import timeit
import matplotlib.pyplot as plt

test_numbers = []

for i in range(1,100):
    rnd = random.random()
    rnd = math.ceil(rnd*pow(10,i))
    if rnd%2==0:
        rnd +=1
    test_numbers.append(rnd)
print(test_numbers)
miller_rabin_times = [float(timeit.timeit('miller_rabin(i)','from __main__ import miller_rabin,i')) for i in test_numbers]
print("MR Done")
trial_division_wheel_factorization_times = [float(timeit.timeit('trial_division_wheel_factorization(i)','from __main__ import trial_division_wheel_factorization,i')) for i in test_numbers]
print("TD Done")
aks_times = [float(timeit.timeit('aks_test(i)','from __main__ import aks_test,i')) for i in test_numbers]

plt.plot(test_numbers,miller_rabin_times,'^b')
plt.plot(test_numbers,aks_times,'sr')
plt.plot(test_numbers,trial_division_wheel_factorization_times,'*g')
plt.xlabel('n')
plt.ylabel('time (in seconds)')
plt.title("Time Taken for different Primality Tests")
plt.legend(['Miller-Rabin',"AKS","Trial Division"])
# plt.legend(['Miller-Rabin',"Trial Division"])
plt.show()
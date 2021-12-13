import math
import numpy as np

def aks_test(n):
    is_prime=True
#All coefficients of (x-1)^n must be divisible by n except for x^n and x^0 to be prime.
    for r in range(1,n):
        coeff = math.comb(n,r)
        if coeff%n!=0:
            is_prime=False
            break
    return is_prime
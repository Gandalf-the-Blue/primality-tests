import math
import numpy as np

def highestPowerOf2(n): 
   return (n & (~(n - 1)))

witnesses = {2047:[2],
            1373653:[2,3],
            9080191:[31,73],
            25326001:[2,3,5],
            3215031751:[2,3,5,7],
            4759123141:[2,7,61],
            1122004669633:[2,13,23,1662803],
            2152302898747:[2,3,5,7,11],
            3474749660383:[2,3,5,7,11,13],
            341550071728321:[2,3,5,7,11,13,17],
            3825123056546413051:[2,3,5,7,11,13,17,19,23],
            18446744073709551616:[2,3,5,7,11,13,17,19,23,29,31,37],
            318665857834031151167461:[2,3,5,7,11,13,17,19,23,29,31,37],
            3317044064679887385961981:[2,3,5,7,11,13,17,19,23,29,31,37,41]
            }

def miller_rabin(n):
    is_prime = True
    if n<=2:
#first checking if n<=2 as then it is obviously prime
        is_prime = True
    else:
#Get number in form of 2^r * d+1 - n
        r = highestPowerOf2(n-1)
        d = int((n-1)/r)
#find bound just larger than n
        dict_key = [k for k in witnesses.keys() if k >=n]
        if not dict_key:
            print("Number too large")
            is_prime=None
        else:
            dict_key = dict_key[0]
#apply (a^d)mod n !=1 to check if composite - if all witnesses say true, then prime.
            for a in witnesses[dict_key]:
                if pow(a,d,n)!=1:
                    is_prime=False
    print(is_prime)
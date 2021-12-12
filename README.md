# Primality Tests

To implement various primality tests and compare speeds of various algorithms.
3 Primality Tests have been implemented - 

# 1. Trial Division with Wheel Factorization

We divide n by numbers \< n and if it is divisible by any number, n is not prime.
To reduce the number of numbers we need to divide by and check, we use two modifications.
All unique factors of n are \< $\sqrt{n} - this is trivial.
Now to further reduce the search space, we use wheel factorization. If a number is not divisible by 2,3 and 5 then if it is represented by $30k+i$ where $i=1,2,3,....29$, i will not be divisible by 2,3, and 5 which rules out quite a few values of i.
We end up with the only allowed i = 1, 7, 11, 13, 17, 19, 23, 29. Thus we only need to check for numbers that are $n (mod 30) =i$. This greatly reduces our state space and helps in improving the speed of the algorithm.

# 2. Miller Rabin Test

We can write the candidate, n as $2^r * d+1$. We then another number $a < n$ and verify if $a^d (mod n) = 1$. If this holds true for the range 2 -> min(n-2, floor(2* (ln(n)^2))). This can get unweildy but for certain limits of n, smaller sets of witnesses are enough to check for primality.

if n < 2,047, it is enough to test a = 2;
if n < 1,373,653, it is enough to test a = 2 and 3;
if n < 9,080,191, it is enough to test a = 31 and 73;
if n < 25,326,001, it is enough to test a = 2, 3, and 5;
if n < 3,215,031,751, it is enough to test a = 2, 3, 5, and 7;
if n < 4,759,123,141, it is enough to test a = 2, 7, and 61;
if n < 1,122,004,669,633, it is enough to test a = 2, 13, 23, and 1662803;
if n < 2,152,302,898,747, it is enough to test a = 2, 3, 5, 7, and 11;
if n < 3,474,749,660,383, it is enough to test a = 2, 3, 5, 7, 11, and 13;
if n < 341,550,071,728,321, it is enough to test a = 2, 3, 5, 7, 11, 13, and 17.
if n < 3,825,123,056,546,413,051, it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, and 23.
if n < 18,446,744,073,709,551,616 = 2^64, it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, and 37.
if n < 318,665,857,834,031,151,167,461, it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, and 37.
if n < 3,317,044,064,679,887,385,961,981, it is enough to test a = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, and 41.

# 3. AKS Test

The AKS Test checks the coefficients of $(x-1)^n - (x^n - 1)$. If all the coefficients are divisible by n, then n is prime.
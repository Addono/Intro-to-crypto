import math
from functools import reduce

import pyprimes as pyprimes

def exp_mod_n(x:int, exp: int, n: int):
    assert x >= 0

    if exp == 0:
        return 1
    elif exp == 1:
        return x % n
    elif exp % 2 == 0:
        return exp_mod_n((x * x) % n, exp // 2, n) % n
    else:
        return (x * exp_mod_n((x * x) % n, (exp - 1) // 2, n)) % n


n = 400428248257
k = 1
for p in pyprimes.erat(25):
    t = math.floor(math.log(n, p))
    k = (k * exp_mod_n(2, p**t, n)) % n

print(math.gcd(n, (k - 1)%n))
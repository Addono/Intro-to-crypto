import math


def Fibonacci(n, m = None, p = False):
    a1 = 0
    a2 = 1

    for j in range(0, n):
        if p:
            print(a2)

        if m is None:
            t = a1 + a2
        else:
            t = (a1 + a2) / m

        a1 = a2
        a2 = t

    return a1


def ext_gcd(a: int, b: int):
    """Implementation for the Extended Euclidean Algorithm as in
    Algorithmic Number Theory v0.65 by Benne de Weger algorithm 2.2"""
    a_prime = int(math.fabs(a))
    b_prime = int(math.fabs(b))
    x1 = 1
    x2 = 0
    y1 = 0
    y2 = 1

    while b_prime > 0:
        q = a_prime // b_prime
        r = a_prime - q * b_prime
        a_prime = b_prime
        b_prime = r
        x3 = x1 - q * x2
        y3 = y1 - q * y2
        x1 = x2
        y1 = y2
        x2 = x3
        y2 = y3

    d = a_prime

    if a >= 0:
        x = x1
    else:
        x = -x1

    if b >= 0:
        y = y1
    else:
        y = -y1

    return {'d': d, 'x': x, 'y': y}
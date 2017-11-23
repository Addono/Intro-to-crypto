def Fibonacci(n, m = None, p = False):
    a1 = 0
    a2 = 1

    for j in range(0, n):
        if p:
            print a2

        if m is None:
            t = a1 + a2
        else:
            t = (a1 + a2) / m

        a1 = a2
        a2 = t

    return a1
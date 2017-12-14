from math import sqrt

print("Fibonacci")

a1 = 0
a2 = 1

for j in range(0, 10):
    print(a2)

    t = a1 + a2
    a1 = a2
    a2 = t

print("\n\nPower root Fibonacci")

a = (1 + sqrt(5)) / 2
b = (1 - sqrt(5)) / 2

for j in range(1, 11):
    print(((a ** j) - (b ** j)) / sqrt(5))


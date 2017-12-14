a1 = 0
a2 = 1

for j in range(0, 20):
    print(a2)

    t = (a1 + a2) % 2
    a1 = a2
    a2 = t

# Stop using ints, switch to reals.
# F_2 / (a^2 + a + 1) gives root
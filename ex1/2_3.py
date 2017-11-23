a1 = 0
a2 = 1

for j in range(0, 20):
    print a2

    t = (a1 + a2) % 2
    a1 = a2
    a2 = t

print "No, since there exists no root for x^2 + x + 1, hence we cannot apply a similar method"
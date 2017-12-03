from crypto.analysis import histogram, frequency
from crypto.cyphers.RC4 import RC4
from crypto.key.generate import generate_key

s2_0 = []
s2_not_0 = []
for _ in range(1000000):
    key = generate_key(16, 8)
    rc4 = RC4(key)
    s2_is_0 = rc4.get_s_index(2) == 0

    if s2_is_0:
        s2_0.append(rc4.generate(2))
    else:
        s2_not_0.append(rc4.generate(2))

frequency.text(s2_0)
frequency.text(s2_not_0)

histogram.plot(s2_0, 256)
histogram.plot(s2_not_0, 256)
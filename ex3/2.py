from crypto.analysis import histogram, frequency
from crypto.cyphers.RC4 import RC4
from crypto.key.generate import generate_key

s2_0 = []
s2_not_0 = []
for _ in range(100000):
    key = generate_key(16, 8)
    rc4 = RC4(key)
    s2_is_0 = rc4.get_s_index(2) == 0

    output = rc4.generate_multiple(2)
    result = output[1]

    if s2_is_0:
        s2_0.append(result)
    else:
        s2_not_0.append(result)

frequency.text(s2_0)
frequency.text(s2_not_0)

histogram.plot(s2_0, 256)
histogram.plot(s2_not_0, 256)
from collections import Counter

from crypto.analysis import histogram, frequency
from crypto.cyphers.RC4 import RC4
from crypto.key.generate import generate_key

result = []
base_key = generate_key(1, 8)
for _ in range(1000000):
    key = base_key + generate_key(15, 8)
    rc4 = RC4(key)

    result.append(rc4.generate())

print(base_key[0])
frequency.text(result)

histogram.plot(result, 256)
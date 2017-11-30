from crypto.analysis import histogram, frequency
from crypto.cyphers.RC4 import RC4
from crypto.key.generate import generate_key

result = []
for _ in range(10000):
    key = generate_key(16, 8)
    rc4 = RC4(key)

    output = rc4.generate_multiple(2)
    result.append(output[1])

frequency.text(result)
histogram.plot(result, 256)
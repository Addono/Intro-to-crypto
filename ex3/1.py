from crypto.analysis import histogram, frequency
from crypto.cyphers.RC4 import RC4
from crypto.key.generate import generate_key

result = []
for _ in range(100000):
    key = generate_key(16, 8)
    rc4 = RC4(key)

    output = rc4.generate(2)
    result.append(output)

frequency.text(result)
histogram.plot(result, 256)
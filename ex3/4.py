from crypto.analysis import histogram, frequency
from crypto.cyphers.RC4 import RC4
from crypto.key.generate import generate_key

result = []
result_sum = []
base_key = generate_key(13, 8)
for _ in range(100000):
    key = generate_key(3, 8) + base_key
    rc4 = RC4(key)

    output = rc4.generate(3)

    result.append(output)
    result_sum.append(sum(key[0:4]) + output)

print(base_key)
frequency.text(result)

histogram.plot(result, 256)
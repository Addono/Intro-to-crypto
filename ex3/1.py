from crypto.cyphers.RC4 import RC4
from crypto.key.generate import generate_key
from collections import Counter

result = []
for _ in range(0, 100000):
    key = generate_key(16, 8)
    rc4 = RC4(key)

    output = rc4.generate_multiple(2)
    result.append(output[1])

c = Counter(result)
print(c.most_common())

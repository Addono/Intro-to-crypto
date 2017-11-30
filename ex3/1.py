from crypto.cyphers.RC4 import RC4

k = [100, 101, 102, 103, 104, 105]

rc4 = RC4(k)

print(rc4.generate())

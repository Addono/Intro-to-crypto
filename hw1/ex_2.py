from tqdm import trange
from crypto.key.generate import generate_key


class RC4_broken:
    def __init__(self, k: list):
        self.__k = k
        self.__S = []
        self.__i = 0
        self.__j = 0

        length = len(k)

        for m in range(256):
            self.__S.append(m)

        n = 0
        for m in range(256):
            n = (n + self.__S[m] + k[m % length]) % 256
            self.swap(m, n)

    def swap(self, m: int, n: int):
        # sn = self.__S[m]
        # self.__S[m] = self.__S[n]
        # self.__S[n] = sn
        self.__S[n] = self.__S[n] ^ self.__S[m]
        self.__S[m] = self.__S[n] ^ self.__S[m]
        self.__S[n] = self.__S[n] ^ self.__S[m]

    def generate(self, amount: int=1):
        for _ in range(amount):
            self.__i = (self.__i + 1) % 256
            self.__j = (self.__j + self.__S[self.__i]) % 256
            self.swap(self.__i, self.__j)

            if self.__i == self.__j:
                return None
        return self.__S[(self.__S[self.__i] + self.__S[self.__j]) % 256]

    def generate_multiple(self, amount: int=1):
        result = []

        for _ in range(amount):
            result.append(self.generate())

        return result

    def get_s_index(self, index: int):
        return self.__S[index]


result = []
iterations = 1000000
for _ in trange(iterations):
    key = generate_key(16, 8)
    rc4 = RC4_broken(key)

    counter = 0
    while rc4.generate() is not None:
        counter += 1

    result.append(counter)

print(result)
print(sum(result)/iterations)

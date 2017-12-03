class RC4:
    S = []
    i = 0
    j = 0

    def __init__(self, k):
        length = len(k)

        for m in range(256):
            self.S.append(m)

        n = 0
        for m in range(256):
            n = (n + self.S[m] + k[m % length]) % 256
            self.swap(m, n)

    def swap(self, m, n):
        sn = self.S[m]
        self.S[m] = self.S[n]
        self.S[n] = sn

    def generate(self, amount=1):
        for _ in range(amount):
            self.i = (self.i + 1) % 256
            self.j = (self.j + self.S[self.i]) % 256
            self.swap(self.i, self.j)
        return self.S[(self.S[self.i] + self.S[self.j]) % 256]

    def generate_multiple(self, amount):
        result = []

        for _ in range(amount):
            result.append(self.generate())

        return result

    def get_s_index(self, index):
        return self.S[index]

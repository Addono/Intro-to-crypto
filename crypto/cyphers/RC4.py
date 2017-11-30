class RC4:
    S = []
    i = 0
    j = 0

    def __init__(self, k):
        l = len(k)

        for i in range(0, 255):
            self.S[i] = i

        j = 0
        for i in range(0, 255):
            j = (j + self.S[i] + k[i % l]) % 256
            self.swap(i, j)

    def swap(self, i, j):
        si = self.S[i]
        self.S[i] = self.S[j]
        self.S[j] = si

    def generate(self):
        self.i = (self.i + 1) % 256
        self.j = (self.j + self.S[self.i]) % 256
        self.swap(self.i, self.j)
        return self.S[(self.S[self.i] + self.S[self.j]) % 256]


class RC4:
    def __init__(self, k):
        self.__S = []
        self.__i = 0
        self.__j = 0

        if type(k) is str:
            k = [ord(char) for char in k]

        length = len(k)

        for m in range(256):
            self.__S.append(m)

        n = 0
        for m in range(256):
            n = (n + self.__S[m] + k[m % length]) % 256
            self.swap(m, n)

    def swap(self, m, n):
        sn = self.__S[m]
        self.__S[m] = self.__S[n]
        self.__S[n] = sn

    def generate(self, amount: int=1):
        for _ in range(amount):
            self.__i = (self.__i + 1) % 256
            self.__j = (self.__j + self.__S[self.__i]) % 256
            self.swap(self.__i, self.__j)
        return self.__S[(self.__S[self.__i] + self.__S[self.__j]) % 256]

    def generate_multiple(self, amount: int=1):
        result = []

        for _ in range(amount):
            result.append(self.generate())

        return result

    def get_s_index(self, index: int):
        return self.__S[index]

    def check_output(self, output: list):
        i = 0
        j = 0
        for expected in output:
            i = (i + 1) % 256
            j = (j + self.__S[i]) % 256
            self.swap(i, j)

            if self.__S[(self.__S[i] + self.__S[j]) % 256] != expected:
                return False

        return True
class RC4:
    def __init__(self, k: list):
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
        S = self.__S
        for expected in output:
            i = (i + 1) % 256
            j = (j + S[i]) % 256

            sj = S[i]
            S[i] = S[j]
            S[j] = sj

            if S[(S[i] + S[j]) % 256] != expected:
                return False

        return True
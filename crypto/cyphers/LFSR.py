class LFSR:
    def __init__(self, key):
        self.key = key
        self.length = len(key)

    def generate(self, state: list):
        assert self.length == len(state)

        count = 0
        for k, s in zip(self.key, state):
            if k == s == 1:
                count += 1

        return state[1:] + [count % 2]

    def sequence_length(self, init_state: list):
        state = init_state
        count = 0
        while True:
            count += 1
            state = self.generate(state)
            if state == init_state:
                return count

    def generate_sequences(self, length: int, base: list = []):
        if length == 0:
            return [base]
        else:
            return self.generate_sequences(length - 1, base + [0]) + self.generate_sequences(length - 1, base + [1])

    def calculate_all_sequence_length(self):
        seq = self.generate_sequences(self.length)
        res = []

        while len(seq) > 0:
            state = init_state = seq[0]
            count = 0
            while True:
                count += 1
                state = self.generate(state)
                seq.remove(state)

                if state == init_state:
                    res.append(count)
                    break

        return sorted(res)
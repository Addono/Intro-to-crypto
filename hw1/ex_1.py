from crypto.cyphers.LFSR import LFSR

l1 = LFSR([1, 1, 1, 0, 0, 1, 0, 0])
print(l1.calculate_all_sequence_length())

l2 = LFSR([1, 0, 0, 1, 0, 0])
print(l2.calculate_all_sequence_length())
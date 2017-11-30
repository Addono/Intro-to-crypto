from random import randint


def generate_key(length, byte_length=8):
    key = []
    max_int_value = 2 ** byte_length

    for i in range(length):
        key.append(randint(0, max_int_value))

    return key

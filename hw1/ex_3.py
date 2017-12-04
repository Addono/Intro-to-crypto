import time

from crypto.cyphers.RC4 import RC4


def increment_key(key: list, l: int = 0, max: int = 256) -> list:
    i = len(key)
    while i > l:
        i -= 1
        key[i] += 1

        if key[i] >= max:
            key[i] = 0
        else:
            return key


def check_key(key: list, expected: list) -> bool:
    rc4 = RC4(key)

    for e in expected:
        if e != rc4.generate():
            return False

    return True


def crack_key(start_key: list, expected_output: list, fixed_digits: int = 0) -> list:
    print(start_key)
    while start_key is not None and not check_key(start_key, expected_output):
        start_key = increment_key(start_key, fixed_digits)

    return start_key

total_key_length = 5
split = 3
given_key_start = [80]
expected_output = [130, 189, 254, 192, 238, 132, 216, 132, 82, 173]

tm = time.time()

given_key_length = len(given_key_start)

start_base_key = given_key_start + [0 for _ in range(split - given_key_length)]
attack_length = total_key_length - split

while start_base_key is not None:
    attack_key = start_base_key + [0 for _ in range(attack_length)] # Generate the key to attack
    crack_key(attack_key, expected_output, split)

    start_base_key = increment_key(start_base_key, given_key_length)

# print(crack_key(start_key, expected_output, 3))


print(time.time() - tm)
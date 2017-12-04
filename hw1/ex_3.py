import concurrent.futures

from tqdm import tqdm

from crypto.cyphers.RC4 import RC4

total_key_length = 5
split = 3
given_key_start = [80]
expected_output = [130, 189, 254, 192, 238, 132, 216, 132, 82, 173]


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


def crack_key(start_key: list) -> list:
    while True:
        if RC4(start_key).check_output(expected_output):
            return start_key

        start_key = increment_key(start_key, split)
        if start_key is None:
            return None


def main():
    given_key_length = len(given_key_start)

    start_extension_length = split - given_key_length
    start_base_key = given_key_start + [0 for _ in range(start_extension_length)]
    attack_length = total_key_length - split
    start_base_key_extension = [0 for _ in range(attack_length)]

    keys = []
    with tqdm(total=256 ** start_extension_length, unit="sub-keys", desc="Adding sub-keys to queue") as pbar:
        while start_base_key is not None:
            attack_key = start_base_key + start_base_key_extension  # Generate the key to attack

            keys.append(attack_key)
            pbar.update(1)

            start_base_key = increment_key(start_base_key, given_key_length)

    results = []
    with concurrent.futures.ProcessPoolExecutor(4) as executor:
        for res in tqdm(executor.map(crack_key, keys), total=len(keys), desc="Processed sub-keys"):
            if res is not None:
                print(res)
                results.append(res)

    print(results)


if __name__ == '__main__':
    main()

import concurrent.futures

from tqdm import tqdm

# Define input parameters
total_key_length = 5    # The total length of the key we want to find.
split = 3               # The amount of digits of the key which make up one task.
given_key_start = [80]  # The part of the key which is given
expected_output = [130, 189, 254, 192, 238, 132, 216, 132, 82, 173]  # The output sequence resulting from the key.

__S = [i for i in range(256)]  # Cache an initial S list.


def increment_key(key: list, l: int = 0, max_value: int = 256) -> list:
    """Increments a key, starting at the largest index. Returns None if no further increments can be made."""
    # Let i point to the last index plus one of the key.
    i = len(key)
    while i > l:  # Only increment indexes which are not within the first l fixed ones.
        # Decrease the index, and increment the key at this index
        i -= 1
        key[i] += 1

        # Check if the key now exceeds the maximum.
        if key[i] >= max_value:
            # Set the corresponding index to zero and increment the next index
            key[i] = 0
        else:
            # We are finished incrementing the key.
            return key

    # Return None in an implicit manner when no new key can be generated.


def rc4_check_key(key: list):
    """"Checks if a key computes the output sequence we want."""
    # Setup key
    S = list(__S) # We have to clone it, else a reference will be used.

    n = 0
    for m in range(256):
        n = (n + S[m] + key[m % total_key_length]) % 256

        # Execute swap
        sn = S[m]
        S[m] = S[n]
        S[n] = sn

    # Check if the output matches.
    i = 0
    j = 0
    for expected in expected_output:
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        # Execute swap
        sj = S[i]
        S[i] = S[j]
        S[j] = sj

        # Check if the generated output mismatches with the expected output.
        if S[(S[i] + S[j]) % 256] != expected:
            # Found a counter example for the current key, hence it is not the key we are looking for.
            return False

    # Current key managed to replicate the expected output, found a key we are looking for.
    return True


def crack_key(key: list) -> list:
    """Returns all keys derived from a given input key which generate the expected output sequence."""
    result = []
    while True:
        if rc4_check_key(key):
            result.append(list(key))

        # Increment key
        i = total_key_length
        while i > split:
            i -= 1
            key[i] += 1

            if key[i] >= 256:
                key[i] = 0
            else:
                break
        else:
            return result


def main():
    """
    Tries to compute the key corresponding with some given output generated with RC4 by brute-force concurrently.
    """
    given_key_length = len(given_key_start)

    start_extension_length = split - given_key_length
    start_base_key = given_key_start + [0 for _ in range(start_extension_length)]
    attack_length = total_key_length - split
    start_base_key_extension = [0 for _ in range(attack_length)]

    # Generate all sub-keys (sub-tasks).
    keys = []
    with tqdm(total=256 ** start_extension_length, unit="sub-keys", desc="Adding sub-keys to queue") as pbar:
        while start_base_key is not None:
            attack_key = start_base_key + start_base_key_extension  # Generate the key to attack

            keys.append(attack_key)
            pbar.update(1)

            start_base_key = increment_key(start_base_key, given_key_length)

    # Check for every sub-key if their resulting set contains a valid key.
    results = []
    with concurrent.futures.ProcessPoolExecutor() as executor:  # Setup concurrency to process the sub-keys in parallel.
        for res in tqdm(executor.map(crack_key, keys), total=len(keys), desc="Processed sub-keys"):
            # Check if the sub-task found a correct key.
            if len(res) > 0:
                print("\n" + str(res))
                results.extend(res)

    # Print the total list of valid keys.
    print(results)


if __name__ == '__main__':
    main()


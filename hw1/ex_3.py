from multiprocessing import Process, Queue, Lock, freeze_support
import time

from tqdm import tqdm

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
    while start_key is not None and not check_key(start_key, expected_output):
        start_key = increment_key(start_key, fixed_digits)

    return start_key


def worker(expected_output, fixed_digits):

    while True:
        start_key = q.get()
        if start_key is None:
            break
        result = crack_key(start_key, expected_output, fixed_digits)
        if result is not None:
            print(result)
        q.task_done()
        pbar.update(1)


if __name__ == '__main__':
    total_key_length = 5
    split = 3
    given_key_start = [80]
    expected_output = [130, 189, 254, 192, 238, 132, 216, 132, 82, 173]
    max_processes = 5

    tm = time.time()

    given_key_length = len(given_key_start)

    start_extension_length = split - given_key_length
    start_base_key = given_key_start + [0 for _ in range(start_extension_length)]
    attack_length = total_key_length - split
    start_base_key_extension = [0 for _ in range(attack_length)]

    # Fill the queue
    q = Queue()
    with tqdm(total=256 ** start_extension_length, unit="sub-keys", desc="Adding sub-keys to queue") as pbar:
        while start_base_key is not None:
            attack_key = start_base_key + start_base_key_extension  # Generate the key to attack

            q.put(attack_key)
            pbar.update(1)

            start_base_key = increment_key(start_base_key, given_key_length)

    # Spawn all processes
    lock = Lock()
    processes = []
    lock.acquire()
    for _ in tqdm(range(max_processes), desc="Spawning processes"):
        process = q.Process(target=worker, args=(expected_output, split))
        process.start()
        process.join()
        processes.append(process)

    pbar = tqdm(total=256 ** start_extension_length)

    # Wait for the queue to be emptied
    q.get()
    pbar.close()

    # Kill all workers
    for _ in tqdm(range(max_processes), desc="Sending kill signal to all workers"):
        q.put(None)
    for t in tqdm(processes, desc="Wait will all workers are finished"):
        t.join()

    print(time.time() - tm)

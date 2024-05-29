import argparse
import random
import statistics
import time
from concurrent.futures import ThreadPoolExecutor

num_trials = 10_000_000


def π(num_trials: int) -> float:
    Ncirc = 0
    ran = random.Random()

    for _ in range(num_trials):
        x = ran.uniform(-1, 1)
        y = ran.uniform(-1, 1)

        test = x * x + y * y
        if test <= 1:
            Ncirc += 1

    return 4.0 * (Ncirc / num_trials)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--threads", type=int, default=0)
    args = parser.parse_args()
    threads = args.threads
    start = time.monotonic()

    if threads == 0:
        pi = π(num_trials)
    else:
        with ThreadPoolExecutor(max_workers=threads) as executor:
            pi = statistics.mean(executor.map(π, [num_trials // threads] * threads))

    stop = time.monotonic()
    print(f"{num_trials} trials, pi is {pi}, {stop - start:.4} s")


if __name__ == "__main__":
    main()

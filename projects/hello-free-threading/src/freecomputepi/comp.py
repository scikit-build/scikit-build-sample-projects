import argparse
import time
import statistics
from concurrent.futures import ThreadPoolExecutor

from ._core import pi

num_trials = 10_000_000


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--threads", type=int, default=0)
    args = parser.parse_args()
    threads = args.threads
    start = time.monotonic()

    if threads == 0:
        π = pi(num_trials)
    else:
        with ThreadPoolExecutor(max_workers=threads) as executor:
            π = statistics.mean(executor.map(pi, [num_trials//threads]*threads))
    
    stop = time.monotonic()
    print(f"{num_trials} trials, {π = }, {stop - start:.4} s")

if __name__ == "__main__":
    main()

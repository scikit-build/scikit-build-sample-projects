import argparse
import statistics
import time
from concurrent.futures import ThreadPoolExecutor

from ._core import pi


def pi_in_threads(threads: int, trials: int) -> float:
    if threads == 0:
        return pi(trials)
    with ThreadPoolExecutor(max_workers=threads) as executor:
        return statistics.mean(executor.map(pi, [trials // threads] * threads))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--threads", type=int, default=0)
    parser.add_argument("--trials", type=int, default=100_000_000)
    args = parser.parse_args()

    start = time.monotonic()
    π = pi_in_threads(args.threads, args.trials)
    stop = time.monotonic()

    print(f"{args.trials} trials, {π = }, {stop - start:.4} s")


if __name__ == "__main__":
    main()

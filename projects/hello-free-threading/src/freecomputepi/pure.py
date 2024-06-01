import argparse
import random
import statistics
import time
from concurrent.futures import ThreadPoolExecutor


def pi(trials: int) -> float:
    Ncirc = 0
    ran = random.Random()

    for _ in range(trials):
        x = ran.uniform(-1, 1)
        y = ran.uniform(-1, 1)

        test = x * x + y * y
        if test <= 1:
            Ncirc += 1

    return 4.0 * (Ncirc / trials)


def pi_in_threads(threads: int, trials: int) -> float:
    if threads == 0:
        return pi(trials)
    with ThreadPoolExecutor(max_workers=threads) as executor:
        return statistics.mean(executor.map(pi, [trials // threads] * threads))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--threads", type=int, default=0)
    parser.add_argument("--trials", type=int, default=10_000_000)
    args = parser.parse_args()

    start = time.monotonic()
    π = pi_in_threads(args.threads, args.trials)
    stop = time.monotonic()

    print(f"{args.trials} trials, {π = }, {stop - start:.4} s")


if __name__ == "__main__":
    main()

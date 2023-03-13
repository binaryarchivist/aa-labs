from typing import List

from sieves.profiler import plot_result
from sieves.algorithms import sieve1, sieve2, sieve3, sieve4, sieve5


def main() -> int:
    inp: List[int] = []
    for _ in range(0, 1000, 10):
        # sieve1(_)
        # sieve2(_)
        # sieve3(_)
        # sieve4(_)
        sieve5(_)
        inp.append(_)
    plot_result(inp)
    return 0


main()

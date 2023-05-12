from sieves.profiler import plot_result, exec_time
from mpmath import mp


@exec_time("bbp_algorithm")
def bbp(n):
    pi = sum(1 / 16 ** k *
             (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
             for k in range(n))
    return pi


@exec_time("leibniz_pi")
def leibniz_pi(n):
    pi = 0
    for i in range(n):
        pi += ((-1) ** i) / (2 * i + 1)
    pi *= 4
    return pi


@exec_time("chudnovsky_algorithm")
def chudnovsky(n):
    mp.dps = n + 1
    C = 426880 * mp.sqrt(10005)
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L
    for _ in range(1, n):
        M = (K ** 3 - 16 * K) * M // K ** 3
        L += 545140134
        X *= -262537412640768000
        S += (M * L) // X
        K += 12
    return C / S


def main() -> int:
    inp = []

    for n in range(0, 3000, 10):
        print("---")
        print(n)
        bbp(n)
        leibniz_pi(n)
        chudnovsky(n)
        inp.append(n)

    plot_result(inp)
    return 0


main()

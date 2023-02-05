import math
import time
from typing import List, Callable
from prettytable import PrettyTable
from decimal import Decimal
import matplotlib.pyplot as plt

import sys

sys.setrecursionlimit(1500)


# recursive
def rec_fib(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)


# iteration
def iter_fib(n: int) -> int:
    a: int = 0
    b: int = 1
    for _ in range(n):
        a, b = b, a + b
    return a


# dynamic programming
def dp_fib(n: int) -> int:
    f: List[int] = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


# Binet's formula, I've used decimal since python has some troubles with big numbers
def binets_fib(n: int) -> any:
    sqrt_5 = math.sqrt(5)
    phi = (Decimal(1) + Decimal(sqrt_5)) / 2
    psi = (Decimal(1) - Decimal(sqrt_5)) / 2
    return int((phi ** Decimal(n) - psi ** Decimal(n)) / Decimal(sqrt_5))


# matrix multiplication
def matrix_fib(n: int) -> int:
    def matrix_mult(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        C = [[0, 0], [0, 0]]
        C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
        C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
        C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
        return C

    def matrix_pow(A: List[List[int]], n: int) -> List[List[int]]:
        if n <= 1:
            return A
        elif n % 2 == 0:
            return matrix_pow(matrix_mult(A, A), n // 2)
        else:
            return matrix_mult(A, matrix_pow(A, n - 1))

    if n <= 0:
        return 0
    else:
        A = [[1, 1], [1, 0]]
        return matrix_pow(A, n - 1)[0][0]


def generate_plot(x_label: str, input: List[int],
                  y_label: str, results: List[float],
                  label: str, color: str,
                  plt_num: int, plt_title: str) -> None:
    plt.figure(plt_num)
    plt.plot(input, results, label=label, color=color)
    plt.title(plt_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)


def get_time(algo: Callable, input_arr: List[int], result: List[float]) -> None:
    start = time.time()
    for i in input_arr:
        algo(i)
        end = time.time()
        result.append(round(end - start, 8))


def main() -> int:
    values: List[int] = [5, 10, 15, 20, 25, 30, 35, 40]
    values2: List[int] = [10000, 15000, 20000, 25000, 50000, 100000, 125000, 150000]

    recursive: List[float] = []
    iterative: List[float] = []
    dynamic: List[float] = []
    binet: List[float] = []
    matrix: List[float] = []

    get_time(rec_fib, values, recursive)
    get_time(iter_fib, values2, iterative)
    get_time(dp_fib, values2, dynamic)
    get_time(binets_fib, values2, binet)
    get_time(matrix_fib, values2, matrix)

    table_recursive = PrettyTable(values)
    table_recursive.add_row(recursive)
    print(table_recursive)

    headers = values2
    table_all = PrettyTable(headers)
    table_all.add_row(iterative)
    table_all.add_row(dynamic)
    table_all.add_row(binet)
    table_all.add_row(matrix)
    print(table_all)

    generate_plot('n_th fib number', values, 'T(n)', recursive, 'Recursive algorithm', 'red', 1, 'Recursive algorithm')
    generate_plot('n_th fib number', values2, 'T(n)', iterative, 'Iterative algorithm', 'green', 2, 'Iterative algorithm')
    generate_plot('n_th fib number', values2, 'T(n)', dynamic, 'DP algorithm', 'blue', 3, 'DP algorithm')
    generate_plot('n_th fib number', values2, 'T(n)', binet, 'Binet\'s formula algorithm', 'black', 4, 'Binet\'s formula algorithm')
    generate_plot('n_th fib number', values2, 'T(n)', matrix, 'Matrix multiplication', 'yellow', 5, 'Matrix multiplication')
    plt.show()
    return 0


if __name__ == "__main__":
    main()

from math import sqrt
from typing import List

from .profiler import exec_time


@exec_time('sieve_1')
def sieve1(n: int) -> List[int]:
    c: List[bool] = [False] + [True] * n
    i: int = 2

    while i <= n:
        if c[i]:
            j = 2 * i
            while j <= n:
                c[j] = False
                j += i
        i += 1

    return c


@exec_time('sieve_2')
def sieve2(n: int) -> List[int]:
    c: List[bool] = [False] + [True] * n
    i: int = 2

    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j += i
        i += 1

    return c


@exec_time('sieve_3')
def sieve3(n: int) -> List[int]:
    c: List[bool] = [False] + [True] * n
    i: int = 2

    while i <= n:
        if c[i]:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j += 1
        i += 1

    return c


@exec_time('sieve_4')
def sieve4(n: int) -> List[int]:
    c: List[bool] = [False] + [True] * n
    i: int = 2

    while i <= n:
        j = 2
        while j < i:
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1

    return c


@exec_time('sieve_5')
def sieve5(n: int) -> List[int]:
    c: List[bool] = [False] + [True] * n
    i: int = 2

    while i <= n:
        j = 2
        while j <= sqrt(i):
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1

    return c

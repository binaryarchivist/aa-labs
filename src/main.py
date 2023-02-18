from typing import List

from sorts.sorting import counting_sort, quick_sort, heap_sort, merge_sort
from sorts.profiler import plot_result
import random

def fill(lst, start, end, count):
    for _ in range(count):
        lst.append(random.randint(start, end))
    return lst

def run_func(func, list) -> None:
    func(list)

def main() -> int:
    my_list = []
    sizes = []

    for i in range(0, 50000, 10000):
        my_list = fill(my_list, -50000, 50000, i)
        run_func(quick_sort, my_list)
        my_list = fill(my_list, -50000, 50000, i)
        run_func(counting_sort, my_list)
        my_list = fill(my_list, -50000, 50000, i)
        run_func(heap_sort, my_list)
        sizes.append(i)

    plot_result(sizes)


    return 0


main()
from typing import List

from sorts.sorting import counting_sort, quick_sort, heap_sort, merge_sort
from sorts.profiler import plot_result
import random

def fill(lst, start, end, count):
    for _ in range(count):
        lst.append(random.randint(start, end))
    return lst

def main() -> int:
    my_list = []
    sizes = []

    for i in range(0, 100000, 10000):
        my_list = fill(my_list, -500000, 500000, i)
        test_arr = my_list
        quick_sort(test_arr)
        # test_arr = my_list
        # merge_sort(test_arr)
        test_arr = my_list
        counting_sort(test_arr)
        test_arr = my_list
        heap_sort(test_arr)
        sizes.append(i)
        print(i)

    # print(my_list)
    plot_result(sizes)


    return 0


main()
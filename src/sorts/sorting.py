from typing import List

from .profiler import exec_time


@exec_time('heap_sort')
def heap_sort(list: List) -> None:
    n = len(list)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Swap the root node with the last node
        list[i], list[0] = list[0], list[i]

        # Heapify the remaining heap
        heapify(list, i, 0)


def heapify(list: List, n, i) -> None:
    largest = i  # Initialize the largest as the root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # If the left child is larger than the root
    if left < n and list[left] > list[largest]:
        largest = left

    # If the right child is larger than the root
    if right < n and list[right] > list[largest]:
        largest = right

    # If the largest is not the root
    if largest != i:
        # Swap the root with the largest element
        list[i], list[largest] = list[largest], list[i]

        # Heapify the affected sub-tree
        heapify(list, n, largest)


@exec_time('quick_sort')
def quick_sort(arr):
    def partition(left, right):
        pivot_index = (left + right) // 2
        pivot_value = arr[pivot_index]
        i = left
        j = right
        while i <= j:
            while arr[i] < pivot_value:
                i += 1
            while arr[j] > pivot_value:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        return i

    def quick_sort_helper(left, right):
        if left < right:
            pivot = partition(left, right)
            quick_sort_helper(left, pivot - 1)
            quick_sort_helper(pivot, right)

    quick_sort_helper(0, len(arr) - 1)


@exec_time('merge_sort')
def merge_sort(list: List) -> None:
    # Base case: return the array if it is empty or has only one element
    if len(list) <= 1:
        return list

    # Divide the array in two halves
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    # Recursively sort the left and right sub-arrays
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge the sorted sub-arrays
    return merge(left_sorted, right_sorted)


def merge(left: List, right: List) -> List:
    result: List = []
    i = j = 0

    # Compare elements from left and right sub-arrays and add the smaller element to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left sub-array
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from the right sub-array
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


@exec_time('counting_sort')
def counting_sort(arr):
    if not arr:
        return

    # Find the minimum and maximum values in the input array
    min_val, max_val = min(arr), max(arr)
    
    # Create a count array of size (max_val - min_val + 1) and initialize all elements to 0
    count = [0] * (max_val - min_val + 1)
    
    # Count the frequency of each element in the input array
    for num in arr:
        count[num - min_val] += 1
    
    # Modify the count array to contain the cumulative sum of the counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Create a new output array of the same size as the input array
    output = [0] * len(arr)
    
    # Place each element in its correct position in the output array
    for num in arr:
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    
    # Shift the output array back by the minimum value to obtain the original values
    for i in range(len(output)):
        output[i] += min_val
    
    return output
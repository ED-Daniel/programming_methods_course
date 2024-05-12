"""
This module contains functions for performing heap sort on an array.

Functions:
    - heapify(arr, n, i): Rearranges the subarray arr[i:] into a heap structure
    - heap_sort(arr): Sorts the given array using heap sort algorithm.

Example usage:
    >>> arr = [4, 10, 3, 5, 1]
    >>> heap_sort(arr)
    >>> print(arr)
    [1, 3, 4, 5, 10]
"""


def heapify(arr, n, i):
    """
    Rearranges the subarray arr[i:] into a heap structure.

    Args:
        arr (list): The input array.
        n (int): The size of the array.
        i (int): The index to start heapifying from.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Sorts the given array using heap sort algorithm.

    Args:
        arr (list): The array to be sorted.
    """
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

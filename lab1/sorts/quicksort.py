def quick_sort(arr):
    """
    Sorts an array using the quick sort algorithm.

    @param arr: The array to be sorted.
    @type arr: list

    @return: The sorted array.
    @rtype: list
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

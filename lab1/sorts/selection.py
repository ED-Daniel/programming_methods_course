def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Находим индекс минимального элемента в оставшейся части массива
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Меняем местами текущий элемент с минимальным элементом
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

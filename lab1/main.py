import time
import matplotlib.pyplot as plt

from loguru import logger

from sorts.heap import heap_sort
from sorts.quicksort import quick_sort
from sorts.selection import selection_sort

from data.read import read_plants_data, select_random_subset


def measure_sorting_time(sort_func, data):
    start_time = time.time()
    sort_func(data)
    end_time = time.time()
    return end_time - start_time


logger.add('times.log')
all_data = read_plants_data('data/plants.csv')
data_lengths = [1000, 5000, 10000, 15000, 20000, 25000, 50000, 75000, 100000]
data_sets = []
for length in data_lengths:
    data_sets.append(select_random_subset(all_data, length))

quicksort_times = []
heapsort_times = []
selectionsort_times = []

for data in data_sets:
    logger.info(f'Data length: {len(data)}')
    quicksort_times.append(measure_sorting_time(quick_sort, data))

    qs_time = quicksort_times[-1]
    logger.info(f'QS Time: {qs_time} seconds')

    heapsort_times.append(measure_sorting_time(heap_sort, data))

    heapsort_time = heapsort_times[-1]
    logger.info(f'HS Time: {heapsort_time} seconds')

    selectionsort_times.append(measure_sorting_time(selection_sort, data))

    selectionsort_time = selectionsort_times[-1]
    logger.info(f'SS Time: {selectionsort_time} seconds')

plt.plot(data_lengths, quicksort_times, label="Quicksort")
plt.plot(data_lengths, heapsort_times, label="Heapsort")
plt.plot(data_lengths, selectionsort_times, label="Selectionsort")
plt.xlabel("Data Length")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithms Comparison")
plt.legend()
plt.savefig('plot.png')
plt.show()

import random
import time
import matplotlib.pyplot as plt

from algos.bin_tree import BinarySearchTree
from data.gen import generate_objects_array, generate_combinations
from algos.hash import HashTable
from algos.red_black_tree import RedBlackTree

from loguru import logger

import sys
sys.setrecursionlimit(20000)
logger.add('main.log')


# Сравнительное время поиска на разных размерностях массива
def compare_search_time(sizes):
    binary_tree_time = []
    red_black_tree_time = []
    hashtable_time = []
    keys = generate_combinations()

    for size in sizes:
        objects = generate_objects_array(size)
        key = random.choice(keys)

        logger.info(f'{size} - {key}')

        binary_tree = BinarySearchTree()
        for obj in objects:
            try:
                binary_tree.insert(obj["key"], obj["value"])
            except Exception:
                break

        binary_tree_start_time = time.time()
        try:
            binary_tree.search(key)
        except Exception:
            logger.error('Max recursion depth')
        binary_tree_end_time = time.time()
        binary_tree_time.append(binary_tree_end_time - binary_tree_start_time)

        logger.info(f'Binary time: {binary_tree_time[-1]}')

        hashtable = HashTable(size)
        for obj in objects:
            hashtable.insert(obj["key"], obj["value"])

        hashtable_start_time = time.time()
        hashtable.search(key)
        hashtable_end_time = time.time()
        hashtable_time.append(hashtable_end_time - hashtable_start_time)

        logger.info(f'Hash time: {hashtable_time[-1]}')

        red_black_tree = RedBlackTree()
        for obj in objects:
            red_black_tree.insert(obj["key"], obj["value"])

        red_black_tree_start_time = time.time()
        red_black_tree.search(key)
        red_black_tree_end_time = time.time()
        red_black_tree_time.append(
            red_black_tree_end_time - red_black_tree_start_time
        )

        logger.info(f'Red black tree time: {red_black_tree_time[-1]}')

    plt.plot(sizes, binary_tree_time, label="Binary Tree")
    plt.plot(sizes, red_black_tree_time, label="Red Black Tree")
    plt.plot(sizes, hashtable_time, label="Hash Table")
    plt.xlabel("Array Size")
    plt.ylabel("Search Time")
    plt.legend()
    plt.savefig("plot.png")
    plt.show()


# Пример использования функций
sizes = [100, 1000, 5000, 10000, 50000, 75000, 100000]
compare_search_time(sizes)

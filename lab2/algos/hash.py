import random


# Реализация хэш таблицы
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None


# Подсчет числа коллизий хэш функц
# ии и построение графика
def count_collisions(size):
    hashtable = HashTable(size)
    keys = ["name", "age", "country"]

    for i in range(size):
        key = random.choice(keys)
        hashtable.insert(key, random.randint(1, 100))

    collisions = 0
    for bucket in hashtable.table:
        if len(bucket) > 1:
            collisions += len(bucket) - 1

    return collisions
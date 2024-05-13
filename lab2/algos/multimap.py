from collections import defaultdict


class MultiMap:
    def __init__(self) -> None:
        self.multi_map = defaultdict(set)

    def insert(self, key, value):
        self.multi_map[key].add(value)

    def search(self, key):
        return self.multi_map[key]

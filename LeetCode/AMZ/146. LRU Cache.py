# https://leetcode.com/problems/lru-cache/
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        try:
            val = self.cache[key]
        except KeyError:
            val = -1

        if val != -1:
            self.cache.move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        existing_val = self.get(key)
        if existing_val != -1:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache.keys()) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value
        # self.cache.move_to_end(key)


if __name__ == '__main__':
    lru = LRUCache(2)

    print(lru.put(2, 1))
    print(lru.put(2, 2))
    print(lru.get(2))
    print(lru.put(1, 1))
    print(lru.put(4, 1))
    print(lru.get(2))

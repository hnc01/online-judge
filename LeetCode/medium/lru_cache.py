'''
    https:#leetcode.com/problems/lru-cache/

    146. LRU Cache

    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

    Implement the LRUCache class:
        - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
        - int get(int key) Return the value of the key if the key exists, otherwise return -1.
        - void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

    The functions get and put must each run in O(1) average time complexity.
'''


class LRUCache:
    data = None
    max_capacity = 0
    cache = None

    def __init__(self, capacity: int):
        self.data = {}
        self.max_capacity = capacity
        self.cache = []

    def get(self, key: int) -> int:
        if key in self.data:
            if key in self.cache:
                # the key is already in the cache so we need to update its position
                self.cache.remove(key)
                self.cache.append(key)
            else:
                # we need to insert it into the cache
                self.cache.append(key)

            return self.data[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            # just update the value, no need to
            self.data[key] = value

            if key in self.cache:
                # the key is already in the cache so we need to update its position
                self.cache.remove(key)
                self.cache.append(key)
            else:
                # we need to insert it into the cache
                self.cache.append(key)
        else:
            if len(self.data) < self.max_capacity:
                self.data[key] = value

                # we just added the key to our data so there's no way it's already in cache
                # we just add it to the cache
                self.cache.append(key)
            else:
                # remove the least used and then put current key
                # we remove the element at cache[0]
                key_to_remove = self.cache[0]

                self.cache.pop(0)

                self.data.pop(key_to_remove)

                self.data[key] = value

                # we just added the key to our data so there's no way it's already in cache
                # we just add it to the cache
                self.cache.append(key)


lRUCache = LRUCache(2)
lRUCache.put(1, 1)  # cache is {1=1}
lRUCache.put(2, 2)  # cache is {1=1, 2=2}
print(lRUCache.get(1))  # return 1
lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))  # returns -1 (not found)
lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))  # return -1 (not found)
print(lRUCache.get(3))  # return 3
print(lRUCache.get(4))  # return 4

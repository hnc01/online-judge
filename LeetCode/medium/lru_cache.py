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


# the below is done using linked lists
class LRUCache2:
    class ListNode:
        def __init__(self, val):
            self.val = val
            self.next = None
            self.previous = None

    cache = None
    cacheKeyToList = None

    head = None
    tail = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # maps every cache key to an element in the linkedList `head`
        self.cacheKeyToList = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            # push the listnode item to the beginning of the list
            # because it was just used
            keyNode = self.cacheKeyToList[key]

            self.markAsUsed(keyNode)

            return self.cache[key]

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # we are updating an existing value so we don't need to check capacity
            self.cache[key] = value

            # update the position of the node in the list
            keyNode = self.cacheKeyToList[key]

            self.markAsUsed(keyNode)
        else:
            # we need to check the capacity
            if len(self.cache) == self.capacity:
                # we need to evict before adding this value
                # we need to find the key at the tail of our linkedlist
                toEvictKey = self.tail.val

                # remove the node from the list
                # if the node was the only one in the list, then we just need to set
                # head and tail to None
                if self.tail == self.head:
                    self.tail = None
                    self.head = None
                else:
                    # we know there is more than 1 node
                    self.tail.next.previous = None
                    self.tail = self.tail.next

                # remove the key from the cache
                del self.cache[toEvictKey]

            # after making room for the new node if there was no room, we add it

            # we have enough room to add this element directly
            self.cache[key] = value
            node = self.ListNode(key)

            # we might not already have a head
            if self.head is not None:
                # add the node to the head directly
                node.previous = self.head
                self.head.next = node
                self.head = node
            else:
                self.head = node
                self.tail = node

            self.cacheKeyToList[key] = node

    def markAsUsed(self, node):
        # if node was already the head then we don't need to make any changes
        if self.head != node:
            # we need to push it to the front
            if node.previous is not None:
                node.previous.next = node.next
            else:
                # the node we're updating was the tail so we need to update tail
                self.tail = node.next

            node.next.previous = node.previous
            self.head.next = node
            node.previous = self.head
            node.next = None
            # make this node the head because it was just used
            self.head = node


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

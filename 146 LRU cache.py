"""

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value =  value
        self.prev = None
        self.next = None



class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

        #left = less recently use
        #right = most recently use

    def remove(self, node): # remove node from list
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node): # insert node at right
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev =nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1




    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
# implementation of lru cache using doubly linked list in O(1) time

class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRU:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]
    
    def _remove(self, node: Node) -> None:
        pv = node.prev
        nx = node.next
        pv.next = nx
        nx.prev = pv
        node.next = None
        node.prev = None

    def _add(self, node: Node) -> None:
        pv = self.tail.prev
        pv.next = node
        node.prev = pv
        node.next = self.tail
        self.tail.prev = node
    
    def debug(self) -> dict:
        # print(self.cache)
        for k in self.cache:
            print("key:", k, "value", self.cache[k].value)
        print("")

lru = LRU(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1)) # 1
lru.put(3, 3)
print(lru.get(2)) # -1
lru.put(4, 4)
print(lru.get(1)) # -1
print(lru.get(3)) # 3
print(lru.get(4)) # 4

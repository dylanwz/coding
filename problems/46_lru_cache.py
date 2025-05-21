'''
# TAG-DLL
# N.B. doubly-linked list + hash map (because we need values, not memory addresses)
# allows O(1) re-arranging
'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # dummy head and tail:
        # H <--(everything in-between)--> T
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # now to update, we can just remove and then add
    def _add(self, node):
        nxt = self.node.next
        self.head.next = node

        node.prev = self.head
        node.next = nxt

        nxt.prev = node
    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        # Move the accessed node to the front
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing node and move to front
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add(node)
        else:
            # Add new node
            if len(self.cache) >= self.capacity:
                # Remove from back
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)
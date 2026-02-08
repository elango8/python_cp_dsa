from threading import Lock

# ===== YOUR CODE (UNCHANGED) =====
class Node:
    def _init_(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def _init_(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_end(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
# ===== END OF YOUR CODE =====


# ===== WRAPPER (SAFE, CLEAN) =====
class LRUCache:
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.map = {}  # key → Node
        self.dll = DoublyLinkedList()
        self.lock = Lock()

    def get(self, key):
        with self.lock:
            if key not in self.map:
                return None

            node = self.map[key]
            self.dll.remove(node)
            self.dll.add_to_end(node)
            return node.value

    def put(self, key, value):
        with self.lock:
            if key in self.map:
                node = self.map[key]
                self.dll.remove(node)
            else:
                if len(self.map) >= self.capacity:
                    # Evict LRU (head.next)
                    lru = self.dll.head.next
                    self.dll.remove(lru)
                    self.map.pop(lru.key)

                node = Node(key, value)
                self.map[key] = node

            self.dll.add_to_end(node)

    def invalidate_prefix(self, prefix: str):
        with self.lock:
            keys = [k for k in self.map if k.startswith(prefix)]
            for k in keys:
                self.map.pop(k, None)

    def clear(self):
        with self.lock:
            self.map.clear()
            self.dll = DoublyLinkedList()

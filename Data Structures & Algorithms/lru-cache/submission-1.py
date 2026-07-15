class ListNode:
    def __init__(self, key=0, val=0):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val
##VERSION WITH ONLY 1 DUMMY NODE, BETTER TO USE 2 DUMMY NODES
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current = 0
        self.hmap = {}
        self.head = ListNode()
        self.tail = self.head

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            if node is self.tail:
                return node.val
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node = self.hmap[key]
            node.val = value
            if node is not self.tail:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
        elif self.current < self.capacity:
            node = ListNode(key, value)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.hmap[key] = node
            self.current += 1
        else:
            lru = self.head.next
            self.hmap.pop(lru.key)
            self.head.next = lru.next
            if lru.next:
                lru.next.prev = self.head
            else:
                self.tail = self.head
            node = ListNode(key, value)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.hmap[key] = node
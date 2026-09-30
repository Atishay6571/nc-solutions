class LRUCache:
# Use 2 dummy nodes for head and tail
# Recent nodes get added in the last, Old in the front
# HashMap: Key --> ListNode(value)
    def __init__(self, capacity: int):
        self.hmap = {} # used to check whether key in List
        self.tail = ListNode(None, None, None, None)
        self.head = ListNode(self.tail, None, None, None)
        self.tail.prev = self.head
        self.current_capacity = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hmap:
            curr = self.hmap[key]
            self.renew(curr)
            return curr.val
        else:
            return -1
    
    # Renewing LRU logic due to get operation - Ads Node to end of List
    def renew(self, node):        
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        self.tail.prev.nxt = node
        node.prev = self.tail.prev
        node.nxt = self.tail
        self.tail.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            curr = self.hmap[key]
            self.renew(curr)
            curr.val = value

        else:
            if self.current_capacity >= self.capacity:
                node = self.head.nxt
                self.hmap.pop(node.key)
                self.head.nxt = node.nxt
                node.nxt.prev = self.head
                self.current_capacity -= 1
                
            curr = ListNode(self.tail, self.tail.prev, key, value)
            self.hmap[key] = curr
            self.current_capacity += 1
            self.tail.prev.nxt = curr
            self.tail.prev = curr


class ListNode:
    def __init__(self, nxt: ListNode, prev : ListNode, key, val):
        self.key = key # store key to map node back to key for removal
        self.val = val
        self.nxt = nxt
        self.prev = prev
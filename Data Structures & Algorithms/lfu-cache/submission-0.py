class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hmap={} #for linking keys with nodes
        self.useCount={} #STORE ELEMENTS BASED ON FREQUENCY AS A LinkedList
        self.usage=0
        self.min_freq=0  # ADDED: track minimum frequency for O(1) eviction

    def _add_new(self, Node):  # ADDED: helper for new nodes
        Node.freq = 0  # ADDED: start at 0 so increaseFreq moves it to 1
        if 0 not in self.useCount:  # ADDED: create freq 0 bucket if needed
            self.useCount[0] = LinkedList()  # ADDED
        self.useCount[0].addInTheEnd(Node)  # ADDED: park node in freq 0
        self.increaseFreq(Node)  # ADDED: moves 0 → 1
        self.min_freq = 1  # ADDED: new node always has lowest freq

    def increaseFreq(self,Node):
        freq=Node.freq
        freq+=1
        if freq not in self.useCount:
            self.useCount[freq-1].remove(Node)
            if self.useCount[freq-1].head.next==self.useCount[freq-1].tail:  # ADDED: clean up empty bucket
                if self.min_freq==freq-1:  # ADDED: update min_freq if needed
                    self.min_freq+=1  # ADDED
                del self.useCount[freq-1]  # ADDED: delete empty bucket
            self.useCount[freq]=LinkedList()
            self.useCount[freq].addInTheEnd(Node)
            Node.freq+=1
        else:
            self.useCount[freq-1].remove(Node)
            if self.useCount[freq-1].head.next==self.useCount[freq-1].tail:  # ADDED: same cleanup for else branch
                if self.min_freq==freq-1:  # ADDED
                    self.min_freq+=1  # ADDED
                del self.useCount[freq-1]  # ADDED
            self.useCount[freq].addInTheEnd(Node)
            Node.freq += 1  # FIXED: removed stray period that made it a float

    def get(self, key: int) -> int:
        if key in self.hmap:
            Node=self.hmap[key]
            self.increaseFreq(Node)
            return Node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:  # ADDED: edge case, zero capacity
            return
        if key in self.hmap:
            Node=self.hmap[key]
            self.increaseFreq(Node)
            Node.val=value
        elif self.capacity>self.usage:
            Node=ListNode(key,value)
            self.hmap[key]=Node
            self._add_new(Node)  # CHANGED: was self.increaseFreq(Node) which crashes on new nodes
            self.usage+=1
        else:
            Node=self.useCount[self.min_freq].head.next  # CHANGED: tail.prev → head.next for LRU
            self.hmap.pop(Node.key)
            self.useCount[self.min_freq].remove(Node)  # CHANGED: tail.prev → Node, already grabbed above
            if self.useCount[self.min_freq].head.next==self.useCount[self.min_freq].tail:  # CHANGED: minimum → self.min_freq
                del self.useCount[self.min_freq]  # CHANGED: minimum → self.min_freq
            NewNode=ListNode(key,value)  # CHANGED: clearer variable name
            self.hmap[key]=NewNode  # CHANGED: use NewNode
            self._add_new(NewNode)  # CHANGED: was increaseFreq called on ListNode directly

class LinkedList:
    def __init__(self):
        self.head=ListNode()
        self.tail=ListNode()
        self.head.next=self.tail
        self.tail.prev=self.head

    def remove(self,Node):
        Node.prev.next=Node.next
        Node.next.prev=Node.prev

    def addInTheEnd(self,Node):
        self.tail.prev.next=Node
        Node.prev=self.tail.prev
        self.tail.prev=Node
        Node.next=self.tail
        
class ListNode:
    def __init__(self,key=0,val=0):
        self.val=val
        self.key=key
        self.prev=None
        self.next=None
        self.freq=1
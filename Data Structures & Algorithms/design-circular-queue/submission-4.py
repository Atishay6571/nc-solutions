class MyCircularQueue:

    def __init__(self, k: int):
        self.size=k
        self.head=ListNode(0)
        self.tail=self.head
        self.cap=0
    def enQueue(self, value: int) -> bool:
        if self.size>self.cap:
            self.tail.next=ListNode(value)
            self.tail=self.tail.next
            self.cap+=1
            return True
        return False

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head=self.head.next
        self.cap-=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.val

    def isEmpty(self) -> bool:
        if self.cap==0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.cap==self.size:
            return True
        return False

class ListNode:
    def __init__(self, val:int):
        self.next=None
        self.val=val




# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
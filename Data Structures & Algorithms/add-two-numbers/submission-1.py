# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2  
        carry = 0
        head = ListNode()
        node = head
        while node1 and node2:
            value = node1.val + node2.val + carry
            if value > 9:
                carry = 1
                value = value % 10
            else:
                carry = 0
            node.next = ListNode(value)
            node1 = node1.next
            node2 = node2.next
            node = node.next
        while node1:
            value = node1.val + carry
            if value > 9:
                carry = 1
                value = value % 10
            else:
                carry = 0
            node.next = ListNode(value)
            node1 = node1.next
            node = node.next
        while node2:
            value = node2.val + carry
            if value > 9:
                carry = 1
                value = value % 10
            else:
                carry = 0
            node.next = ListNode(value)
            node2 = node2.next
            node = node.next
        if carry:
            node.next = ListNode(1)
        return head.next
        
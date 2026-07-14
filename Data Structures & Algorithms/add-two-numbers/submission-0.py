# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #construct both numbers by traversing the linkedlist
        curr=l1
        a=""
        b=""
        while curr:
            a+=str(curr.val)
            curr=curr.next
        curr=l2
        while curr:
            b+=str(curr.val)
            curr=curr.next
        a=int(a[::-1])
        b=int(b[::-1])
        answer= str(a+b)[::-1]

        first=ListNode(0)
        dummy=first
        for character in answer:
            dummy.next=ListNode(int(character))
            dummy=dummy.next
        return first.next


        
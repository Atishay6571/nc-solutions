# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        ahead=None
        node=head
        stack=[]
        final=[]
        if head==[]:
            return []
        while node:
            ahead=node.next
            node.next=prev
            prev=node
            node=ahead
        return prev
            
            
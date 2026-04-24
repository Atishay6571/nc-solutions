# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node=head
        dummy=ListNode()
        dummy.next=head
        prev= dummy
        ptr=1
        #isolating and searching boundaries
        while node:

            if ptr==left:
                saveLeft=prev
            
            if ptr==right:
                saveRight=node.next

            prev=node
            node=node.next
            ptr+=1
        #reversing
        ptr=1
        node=head
        prev=saveRight
        while node:
            ahead=node.next

            if left<=ptr<=right:
                node.next=prev
                prev=node
            
            if ptr==right:
                saveLeft.next=node
               

            node=ahead
            ptr+=1

        return dummy.next

            

            

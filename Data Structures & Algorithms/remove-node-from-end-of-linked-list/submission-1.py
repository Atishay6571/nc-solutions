# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt=1
        node=head
        nodes=[]
        while node:
            nodes.append(node)
            node=node.next
        length=len(nodes)
        node=head
        rmv=length-n+1
        if rmv==1:
            return head.next
        while node:
            cnt+=1
            prev=node
            node=node.next
            if cnt==rmv:                
                prev.next=node.next
                return head


            

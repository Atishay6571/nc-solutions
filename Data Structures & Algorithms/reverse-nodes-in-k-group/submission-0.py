# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #need to check if next k elements even exist
        curr=head
        dummy=ListNode(0,head)
        groupPrev=dummy
        while True:
            kth=self.kth(curr,k)
            if not kth:
                break
            groupNext=kth.next
            result=self.reverseList(curr,k,groupNext)
            groupPrev.next=kth
            groupPrev=result
            curr=groupNext
        return dummy.next

        
    def kth(self, curr, k):
        while curr and k>1:
            k-=1
            curr=curr.next
        return curr
    def reverseList(self,head,k,prev):
        #logic to reverse only k elements
        tail=head

        for i in range(k):
            ahead=head.next
            head.next=prev
            prev=head
            head=ahead
        
        return tail
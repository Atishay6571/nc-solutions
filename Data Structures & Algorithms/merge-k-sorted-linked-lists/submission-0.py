# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists)>1:
            mergedLists=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if len(lists)>i+1 else None
                mergedLists.append(self.mergeList(l1,l2))
            lists=mergedLists
        if not lists:
            return None
        return lists[0]
    def mergeList(self,l1,l2):
        #merge 2 sorted lists
        dummy=ListNode()
        head=dummy
        while l1 and l2:
            if l1.val>l2.val:
                dummy.next=l2
                l2=l2.next
            else:
                dummy.next=l1
                l1=l1.next
            dummy=dummy.next
        while l1:
            dummy.next=l1
            l1=l1.next
            dummy=dummy.next
        while l2:
            dummy.next=l2
            l2=l2.next
            dummy=dummy.next
        return head.next
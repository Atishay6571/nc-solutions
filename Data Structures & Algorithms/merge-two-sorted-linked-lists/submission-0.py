# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head=None
        if list1==None:
            return list2
        elif list2==None:
            return list1

        if list1.val<list2.val:
            prev=list1
            node1=list1.next
            node2=list2
            head=list1
        else:
            prev=list2
            node2=list2.next
            node1=list1
            head=list2

        while node1 and node2:

          max1=node1.val
          max2=node2.val
          if max1<max2:
            prev.next=node1
            prev=node1
            node1=node1.next
          else:
            prev.next=node2
            prev=node2
            node2=node2.next
        if node1==None:
            prev.next=node2
        elif node2==None:
            prev.next= node1
        return head
            
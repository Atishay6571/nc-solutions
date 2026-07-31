# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node=head
        while node.next:
            ahead= node.next
            gcd = math.gcd(ahead.val, node.val)
            node.next = ListNode(gcd, ahead)
            node=ahead
        return head

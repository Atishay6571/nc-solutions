"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes=[]
        node=head
        hmap={}
        if head==None:
            return None
        while node:
            nodes.append(node)
            node=node.next
        newNodes=[]
        prev=Node(nodes[0].val)
        newNodes.append(prev)
        hmap[nodes[0]]=prev
        for i in range(1,len(nodes)):
            val=nodes[i].val
            ptr=Node(val)
            prev.next=ptr
            prev=ptr
            newNodes.append(ptr)
            hmap[nodes[i]]=ptr

        for i in range(0, len(nodes)):
            print(i)
            if nodes[i].random!=None:
                newNodes[i].random=hmap[nodes[i].random]
        print(newNodes[0])
            
        return newNodes[0]
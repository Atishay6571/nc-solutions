"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #a hash map so that keys can be old nodes and values are new 
        hmap={}
        def dfs(node):
            for neighbor in node.neighbors:
                if neighbor not in hmap:
                    hmap[neighbor]=Node(neighbor.val)
                    dfs(neighbor)
                hmap[node].neighbors.append(hmap[neighbor])
        if not node:
            return None
        hmap[node]=Node(node.val)

        dfs(node)
        return hmap[node]

        


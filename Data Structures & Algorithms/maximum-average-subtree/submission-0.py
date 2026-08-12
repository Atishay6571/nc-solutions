# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        
        maximum = [0]
        def dfs(node):
            if not node:
                return 0, 0 # sum, no of nodes
            s1, n1 = dfs(node.left)
            s2, n2 = dfs(node.right)
            curr = (s1+s2+node.val)
            maximum[0] = max(maximum[0], curr/ (n1+n2+1))
            return curr, (n1+n2+1)
        dfs(root)
        return maximum[0]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #PRE-ORDER where root is the depth and we count from Top to Bottom
        result=[0]
        def dfs(node,depth):
            if not node:
                result[0]= max(result[0],depth)
                return
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        return result[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    import math
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #top to bottom
        def dfs(node, lower,upper):
            if not node: return True
            if lower<node.val<upper:
                return dfs(node.left,lower,node.val) and dfs(node.right,node.val,upper)
            else:
                return False
        return dfs(root,-math.inf,math.inf)

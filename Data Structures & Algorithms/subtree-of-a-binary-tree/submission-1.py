# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(p,q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            l=same(p.left,q.left)
            r=same(p.right,q.right)
            if p.val==q.val and l and r:
                return True
            else:
                return False
        
        def dfs(node):
            if not node:
                return False
            l=dfs(node.left)
            r=dfs(node.right)
            if l or r:
                return True
            if node.val==subRoot.val:
                return same(node,subRoot)
            else:
                return False
        return dfs(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #OPTIMIZED APPROACH - utilizing the bst property:
        result=[0]
        def dfs(node):
            if not node: return None
            if p.val<=node.val<=q.val:
                result[0]=node
            elif p.val>=node.val>=q.val:
                result[0]=node
            elif q.val>node.val and p.val>node.val:
                dfs(node.right)
            elif p.val<node.val and q.val<node.val:
                dfs(node.left)
        dfs(root)
        return result[0]
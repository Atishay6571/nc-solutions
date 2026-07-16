# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maximum=root.val
        results=[0]
        def dfs(node,maximum):
            if not node:
                return 0
            if maximum<=node.val:
                maximum=node.val
                results[0]+=1
            l=dfs(node.left,maximum)
            r=dfs(node.right,maximum)

        dfs(root,maximum)
        return results[0]
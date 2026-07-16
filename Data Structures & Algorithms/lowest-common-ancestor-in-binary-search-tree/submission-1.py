# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        result=[None]
        def dfs(node):
            if not node: return 0
            l=dfs(node.left)
            r=dfs(node.right)

           #If both left and right are coming as True, we have our answer
            if l==-1 and r==-1:
                result[0]=node
                return 0

            #If one node is ancestor of other and gets caught
            if l==-1 or r==-1:
                if node.val==q.val or node.val==p.val:
                    result[0]=node
                    return 0
                else:
                    return -1
                
            #If node matches value then keep returning
            if node.val==p.val or node.val==q.val:
                return -1
            
 

        dfs(root)
        return result[0]
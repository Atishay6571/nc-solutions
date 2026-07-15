# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #ITERATIVE APPRAOCH - with stacks
        stack=[]
        result=[]
        if not root:
            return []
        stack.append(root)
        while stack:
            Node=stack.pop()
            if Node.right:
                stack.append(Node.right)
            if Node.left:
                stack.append(Node.left)
            result.append(Node.val)
        return result
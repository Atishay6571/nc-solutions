# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # run dfs continously
        pairs = [] 
        def getHeight(node):
            if node is None:
                return -1
            currHeight = max(getHeight(node.right), getHeight(node.left))+1
            pairs.append((currHeight, node.val))
            return currHeight
        
        getHeight(root)
        pairs.sort()
        n = len(pairs)
        i=0
        height = 0

        solution=[]
        while i<n:
            nums = []
            while i<n and pairs[i][0]==height:
                nums.append(pairs[i][1])
                i+=1
            solution.append(nums)
            height+=1
        return solution


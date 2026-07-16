# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #to return right most, we must use BFS and return the last popped
        queue=collections.deque()
        queue.append(root)
        results=[]
        if not root:
            return []
        while queue:
            total=len(queue)
            for i in range(total):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i==total-1:
                    results.append(node.val)
        return results
                
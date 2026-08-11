# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.index = -1
        self.queue = []
        def construct(node):
            if not node:
                return
            construct(node.left)
            self.queue.append(node)
            construct(node.right)

        construct(root)

    def next(self) -> int:
        self.index+=1
        return self.queue[self.index].val
    def hasNext(self) -> bool:
        if self.index+1 < len(self.queue):
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
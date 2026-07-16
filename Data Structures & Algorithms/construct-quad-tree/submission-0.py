"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n=len(grid)
        def dfs(n,r,c):
            val=True
            for i in range(n):
                for j in range(n):
                    if grid[r][c]!=grid[r+i][c+j]:
                        val=False
                        break
                if not val:
                    break
            if val:
                return Node(grid[r][c], True, None, None, None, None)
            else:
                topLeft=dfs(n//2,r,c)
                topRight=dfs(n//2,r,c+n//2)
                bottomLeft=dfs(n//2,r+n//2,c)
                bottomRight=dfs(n//2,r+n//2,c+n//2)
                return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(n,0,0)
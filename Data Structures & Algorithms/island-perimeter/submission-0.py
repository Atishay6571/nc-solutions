class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #given a grid. to find perimeter: if water or bounds then add peri+=1
        rows=len(grid)
        cols=len(grid[0])
        visited=set() #values in the form of (r,c)
        perimeter=[0]
        def dfs(r,c):
            #base case: ig anything goes wrong, return True or False
            if (r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0):
                return 1
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            up=dfs(r+1,c)
            down=dfs(r-1,c)
            right=dfs(r,c+1)
            left=dfs(r,c-1)
            perimeter[0]+=(up+down+right+left)
            return 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    dfs(r,c)
                    return perimeter[0]

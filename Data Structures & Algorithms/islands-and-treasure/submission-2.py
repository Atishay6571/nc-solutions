class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        rows=len(grid)
        cols=len(grid[0])
        dr=[(-1,0),(1,0),(0,-1),(0,1)]
        def bfs(row,col,dist):
            queue=deque([(row,col,dist)]) #(r,c)
            visited=set()
            visited.add((row,col))
            while queue:
                r,c,dist=queue.popleft()
                for newr,newc in dr:
                    if (0<=r+newr<rows and 0<=c+newc<cols and grid[r+newr][c+newc]!=-1 and (r+newr,c+newc) not in visited):
                        visited.add((r+newr,c+newc))
                        queue.append((r+newr,c+newc,dist+1))
                if grid[r][c]==0:
                    #cant return raw distance as water may be present
                    grid[row][col]=(dist)
                    break
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]>10000:
                    bfs(r,c,0)
        
#for bfs: i want to pop nodes, check if treasure, if yes return else continue, track depth return

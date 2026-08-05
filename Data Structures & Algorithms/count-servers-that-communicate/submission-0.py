class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        rows, cols= len(grid), len(grid[0])
        def dfs(r,c , dr,dc):
            if grid[r][c]==1:
                return True
            nr, nc= dr+r, dc+c
            if (nr<0 or nc< 0 or nr>= rows or nc>=cols):
                return False
            return dfs(nr,nc, dr,dc)
        count=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    for dr, dc in directions:
                        nr, nc = dr+r, dc+c
                        if (nr>=0 and nc>= 0 and nr< rows and nc< cols) and dfs(r+dr,c+dc, dr,dc):
                            count+=1
                            break
        return count
        
                
            
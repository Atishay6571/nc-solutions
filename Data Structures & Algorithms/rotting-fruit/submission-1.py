class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        queue=deque()
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c))
        #now multi source bfs from all rotten bananas
        minutes=-1
        while queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                for dr,dc in directions:
                    if (r+dr<0 or c+dc<0 or r+dr>=rows or c+dc>=cols
                    or grid[r+dr][c+dc] in [0,2]):
                        continue                
                    queue.append((r+dr,c+dc))
                    grid[r+dr][c+dc]=2
            minutes+=1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1
        return max(minutes,0)
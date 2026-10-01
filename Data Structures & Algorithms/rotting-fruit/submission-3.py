class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r,c])
        minutes = -1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nr >= rows or nc < 0 or nc>= cols or grid[nr][nc] in [0,2]):
                        continue
                    queue.append([nr,nc])
                    grid[nr][nc] = 2

            minutes += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return max(minutes,0)

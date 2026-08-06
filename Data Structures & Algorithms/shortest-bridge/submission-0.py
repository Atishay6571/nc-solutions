class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # minimum cost to reach another island
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        visit = set()
        def dfs(r,c):
            grid[r][c] = -1
            visit.add((r,c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (nr<0 or nc<0 or nc== cols or nr == rows or (nr, nc) in visit):
                    continue
                if grid[nr][nc]==0:
                    queue.append((nr,nc))
                else:
                    dfs(nr, nc)
        def bfs():
            visited = set()
            count = 0 
            while queue: 
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    if (r,c) in visited:
                        continue
                    visited.add((r,c))
                    if grid[r][c] ==1 :
                        return count
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if (nr<0 or nc<0 or nc== cols or nr == rows or grid[nr][nc]==-1):
                            continue
                        queue.append((nr,nc))

                count+=1
            return count
        flag = True
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    dfs(r,c)
                    flag = False
                    break
            if not flag:
                break
        return bfs()

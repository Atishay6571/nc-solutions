class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        maxHeap = [] # as we want to pop the max valuye first
        directions= [(1,0),(-1,0),(0,1),(0,-1)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs():
            heapq.heappush(maxHeap, (-grid[0][0], 0, 0))
            while maxHeap:
                score, r,c = heapq.heappop(maxHeap)
                score = -score
                if (r,c) in visited:
                    continue
                visited.add((r,c))
                if r== rows - 1 and c == cols-1:
                    return score
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (nr<0 or nc<0 or nr>= rows or nc >= cols):
                        continue
                    heapq.heappush(maxHeap, (- min(score, grid[nr][nc]), nr, nc))
        
        return bfs()

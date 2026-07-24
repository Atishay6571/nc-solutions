class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #djikstra's: to reach a node, max cost
        minHeap=[(grid[0][0],0,0)] #(height,r,c)
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=set()
        rows,cols=len(grid), len(grid[0])
        while minHeap:
            height, r, c = heapq.heappop(minHeap)
            if (r,c) in visited:
                continue
            if (r==rows-1 and c==cols-1):
                return height
            visited.add((r,c))
            for dr, dc in directions:
                nr, nc= r + dr, c+ dc
                if (nr<0 or nc<0 or nr>=rows or nc>=cols):
                    continue
                if (nr,nc) not in visited:
                    cost=max(height,grid[nr][nc])
                    heapq.heappush(minHeap,(cost,nr,nc))
            

            
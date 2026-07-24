class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row,col=len(heights),len(heights[0])
        #djikstra's algo: track the minimum effort to reach a cell
        minHeap=[(0,0,0)] #[effort, row, col] 
        directions=[(-1,0),(1,0),(0,1),(0,-1)]

        #dynamically build heap
        #DJIKSTRA: the first time a node is popped thats the minimum.
        #so once a node is processed, no need to process it ever again
        visited=set()
        while minHeap:
            cell= heapq.heappop(minHeap)
            r,c=cell[1],cell[2]

            #very important as heap might have stale entries as our check is at push time
            #therefore
            if (r,c) in visited:
                continue
            visited.add((r,c))

            if r==row-1 and c==col-1:
                return cell[0]
            for dr,dc in directions:
                newr,newc=r+dr,c+dc
                if (newr<0 or newc<0 or newr>=row or newc>=col ):
                    continue
                effort=abs(heights[r][c]-heights[newr][newc])
                effort=max(effort,cell[0])
                heapq.heappush(minHeap, (effort,newr,newc))
            

                


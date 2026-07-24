class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #djikstra's algo

        minHeap=[(0,points[0][0],points[0][1])] # (distance, row, col)
        processed=0
        cost=0
        visited=set() #must be there to prevent multiple
        #visited.add((points[0][0],points[0][1]))
        while minHeap:
            #base case
            if processed==len(points):
                return cost
            
            node = heapq.heappop(minHeap)
            r,c=node[1],node[2]
            if (r,c) in visited:
                continue
            visited.add((r,c))
            cost+=node[0]
            processed+=1
            
            #now calculate min distance between all points
            for newr,newc in points:
                if (newr,newc) not in visited:
                    distance=(abs(r-newr)+abs(c-newc))
                    heapq.heappush(minHeap,(distance, newr, newc))
            
        return cost
            


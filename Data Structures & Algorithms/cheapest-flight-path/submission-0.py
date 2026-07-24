class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #djikstra but with additional "stop" parameter
        adj=defaultdict(list)
        for u,v,cost in flights:
            adj[u].append((cost,v))
        
        #minHeap to process
        minHeap=[(0,-1,src)] #(cost, stops, dst)
        while minHeap:
            node=heapq.heappop(minHeap)
            cost, stops, airport= node[0], node[1], node[2]

            #base-cases
            if stops>k:
                continue #if stops constraint is violated
            if dst==airport:
                return cost

            for price, neighbor in adj[airport]:
                heapq.heappush(minHeap, (price+cost, stops+1, neighbor))
        return -1
            

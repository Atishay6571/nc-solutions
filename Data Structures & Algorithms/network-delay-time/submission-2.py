class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # djikstra's algorithm
        # track visited, if all nodes visited return
        # similar to bfs because need to track minimum time

        # create adjacency list to visualize graph as well
        adj= defaultdict(list)
        for u,v,t in times:
            adj[u].append((t,v)) # (time to reach, target)
        
        minHeap=[(0,k)] #(time, node)

        #must maintain a visited set to track the first time or arrival
        elapsed=0
        visited=set()
        while minHeap: #some stopping condition
            time, node= heapq.heappop(minHeap)

            #pop-check is important
            if node in visited:
                continue
            visited.add(node)
            for moreTime, neighbors in adj[node]:
                if neighbors not in visited:
                    heapq.heappush(minHeap, (moreTime+time, neighbors))
            if len(visited)==n:
                return time
        return -1
                
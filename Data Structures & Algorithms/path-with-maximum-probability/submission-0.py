class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # each node has a path, return max path possible
        # djikstra's
        maxHeap = [] # (probability, node) must be a max heap to return max prob
        adj= defaultdict(list) #(node, prob)
        visited=set()
        for i, (a,b) in enumerate(edges):
            adj[a].append((b, succProb[i]))
            adj[b].append((a, succProb[i]))

        for n,p in adj[start_node]:
            heapq.heappush(maxHeap, (-p,n))
        
        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            if node in visited:
                continue
            visited.add(node)
            if node == end_node:
                return -prob
            for neighbor, p in adj[node]:
                heapq.heappush(maxHeap, (p*prob, neighbor))
        return 0


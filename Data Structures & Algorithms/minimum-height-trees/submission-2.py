class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #another key idea: leaf nodes can never be the answer so trim them
        adj = defaultdict(list)
        if n == 1:
            return [0]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        queue=deque()
        edge_count=[0]*n
        i=0
        for node in range(n):
            values=adj[node]
            edge_count[node]=len(values)
            if len(values)<2:
                queue.append(node)
        nodes=n
        while nodes>2:
            size=len(queue)
            nodes-=size
            for i in range(size):
                node=queue.popleft()
                
                for neighbor in adj[node]:
                    edge_count[neighbor]-=1
                    if edge_count[neighbor]==1:
                        queue.append(neighbor)
        return list(queue)

            


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #build adjacency list first
        adj=defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        #for height calculation we can run bfs
        def bfs(root):
            queue=deque()
            queue.append(root)
            visited=set() #since graphs are undirected, must track to prevent infinite loops
            visited.add(root)
            height=0
            while queue:
                for i in range(len(queue)):
                    node=queue.popleft()
                    for child in adj[node]:
                        if child not in visited:
                            visited.add(child)
                            queue.append(child)
                height+=1
            return height
        result=defaultdict(list)
        for root in adj:
            height=bfs(root)
            result[height].append(root)
        if edges==[]:
            return [0]
        return result[min(result)]
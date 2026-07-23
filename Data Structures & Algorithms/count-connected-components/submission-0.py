class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #create adjacency list
        adj=defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited=set()
        def dfs(node):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        components=0
        for i in range(n):
            if i not in visited:
                components+=1
                dfs(i)
        return components
        
        
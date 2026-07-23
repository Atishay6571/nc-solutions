class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #KEY IDEA:
        #edges == n-1 AND connected → tree (no cycle possible)
        #edges == n-1 AND not connected → not a tree
        #edges > n-1 → guaranteed cycle → not a tree
        #edges < n-1 → can't be connected → not a tree
        if edges==[]:
            return True

        if len(edges)!=n-1:
            return False
        adjacency=defaultdict(list)
        for a,b in edges:
            adjacency[a].append(b)
            adjacency[b].append(a)

        visited=set()
        def dfs(node):
            for neighbors in adjacency[node]:
                if neighbors not in visited:
                    visited.add(neighbors)
                    dfs(neighbors)
            
        dfs(0)
        if len(visited)==n:
            return True
        return False

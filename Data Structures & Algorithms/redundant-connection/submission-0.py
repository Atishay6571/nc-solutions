class Solution:
    def findRedundantConnection(self, edges):
        adj = defaultdict(list)
        #key idea: detect cycle, process edge one by one

        def dfs(src,target,visited):
            if src==target:  #edges are already connected
                return True
            visited.add(src)
            for neighbor in adj[src]:
                if neighbor not in visited:
                    if dfs(neighbor,target,visited):
                        return True
            return False
        for src,target in edges:
            visited=set()
            if dfs(src,target,visited):
                return [src,target]
            else:
                adj[src].append(target)
                adj[target].append(src)


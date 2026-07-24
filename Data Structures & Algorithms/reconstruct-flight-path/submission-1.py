class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
      # Use  Hierholzer's algorithm  !! Graph Theory- find Eulerian path
        adj = defaultdict(list)
        for depart, arrival in tickets:
            adj[depart].append(arrival)
        
        for key in adj:
            adj[key].sort(reverse=True)  # sort descending so pop() gives smallest
        
        route = []
        def dfs(airport):
            while adj[airport]:
                dfs(adj[airport].pop())  # pop smallest, recurse
            route.append(airport)        # no more flights, add to route
        
        dfs("JFK")
        return route[::-1]     
from collections import defaultdict
class Graph:
    
    def __init__(self):
        self.adjlist=defaultdict(list)

    def addEdge(self, src: int, dst: int) -> None:
      
        if dst not in self.adjlist[src]:
            self.adjlist[src].append(dst)
        self.adjlist[dst]
    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjlist or dst not in self.adjlist[src]: 
            return False
        self.adjlist[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited=set ()
        
        def dfs(node): 
            if node==dst: 
                return True 
            visited.add(node)
            for neighbour in self.adjlist[node]: 
                if neighbour not in visited: 
                    if(dfs(neighbour)): 
                        return True
            
            return False
        
        return dfs(src)


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=defaultdict(list)
        #create adjacency list (neighbor, weight)
        #WEIGHTED GRAPH PROBLEM
        i=0
        for a,b in equations:
            adj[a].append((b,values[i]))
            adj[b].append((a,1/values[i]))
            i+=1
        
        def dfs(a,b,visited,result):
            visited.add(a)
            for neighbor,value in adj[a]:
                if neighbor==b:
                    result*=value
                    return result
                if neighbor not in visited:
                    result*=value
                    capture=dfs(neighbor,b,visited,result)
                    if capture!=-1:
                        return capture
                    result=result/value
            else:
                return -1
        output=[]
        for a,b in queries:
            if a not in adj or b not in adj:
                output.append(-1)
                continue
            elif a==b:
                output.append(1)
                continue

            visited=set()
            output.append(dfs(a,b,visited,1))
        return output
        


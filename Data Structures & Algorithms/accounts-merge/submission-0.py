class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #key idea, each email are connected as graphs
        adj=defaultdict(list)

        #create adjacency list to join all emails in a graph
        emailUsers=defaultdict(str)


        for account in accounts:
            for i in range(1,len(account)-1):
                adj[account[i]].append(account[i+1])
                adj[account[i+1]].append(account[i])
                
            for i in range(1,len(account)):
                #dictionary to map emails to usernames
                emailUsers[account[i]]=account[0]
        
        #collect connected components
        def dfs(email,visited,results):
            for neighbor in adj[email]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    results.append(neighbor)
                    dfs(neighbor,visited,results)
            return results
        #iterate over all emails
        visited=set()
        output=[]
        for key in emailUsers:
            if key not in visited:
                visited.add(key)
                result=dfs(key,visited,[key])
                result.sort()
                result=[emailUsers[key]]+result
                output.append(result)
        return output


        

        

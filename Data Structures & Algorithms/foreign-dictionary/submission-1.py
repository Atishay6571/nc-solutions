class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj=defaultdict(list)
        #Kahn's algo- removal of leaf nodes
        unique=set()
        for word in words:
            for char in word:
                unique.add(char)
        #construction of adjacency list
        for i in range(len(words)-1):
            for j in range(min(len(words[i]),len(words[i+1]))):

                if words[i][j]==words[i+1][j]:
                    continue
                adj[words[i][j]].append(words[i+1][j])
                break
            else:
                if len(words[i])>len(words[i+1]):
                    return ""
        indegree={ ch : 0 for ch in unique}  #kahns algorithm requires indegree
        for keys in adj:
            for values in adj[keys]:
                indegree[values]+=1
        
        #Now start with kahn's- Queue nodes with indegree=0
        queue=deque()
        result=""
        for char in indegree:
            if indegree[char]==0:
                queue.append(char)
        while queue:
            char=queue.popleft()
            result+=char
            for values in adj[char]:
                indegree[values]-=1
                if indegree[values]==0:
                    queue.append(values)
        if len(result)!=len(unique):
            return ""
        return result



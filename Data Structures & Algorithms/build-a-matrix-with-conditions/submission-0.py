class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        #similar to the course schedule problem
        # calculate indegree
        row_indeg=[0]*k
        row_adj=defaultdict(list)
        for up,down in rowConditions:
            row_adj[up-1].append(down-1) # up ---> down
            row_indeg[down-1]+=1
        col_indeg=[0]*k
        col_adj=defaultdict(list)
        for left,right in colConditions:
            col_adj[left-1].append(right-1) # left ---> right
            col_indeg[right-1]+=1
        def Kahns(indeg,adj):
            queue=deque()
            for i in range(len(indeg)):
                if indeg[i]==0:
                    queue.append(i)
            processed=0
            result=[0]*k ## the kth elements row/col position would be at res[k]
            while queue:
                node=queue.popleft()
                result[node]=processed
                processed+=1
                for neighbours in adj[node]:
                    indeg[neighbours]-=1
                    if indeg[neighbours]==0:
                        queue.append(neighbours)
            if processed==k:
                return result
            return []
        matrix = [[0]*k for _ in range(k)]        
        rowindex= Kahns(row_indeg,row_adj)
        colindex= Kahns(col_indeg,col_adj)
        if rowindex !=[] and colindex !=[]:
            for i in range(k):
                matrix[rowindex[i]][colindex[i]]=i+1
        else:
            return []
        return matrix

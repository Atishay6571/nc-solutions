class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #starting from the boundary and marking all sets reachable
        pac,atl=set(),set()
        rows,cols=len(heights),len(heights[0])

        def dfs(r,c,visit,prevheight):
            if (r<0 or c<0 
                or r==rows or c==cols
                or (r,c) in visit
                or heights[r][c]<prevheight):
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        result=[]
        for ans in pac:
            if ans in atl:
                result.append(ans)
        return result
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        result=[]
        visited=set()
        #helper functions to check for pacific or atlantic        
        def pacific(r,c):
            if (r==0 or c==0):
                return True
            return False
        def atlantic(r,c):
            if (r==rows-1 or c==cols-1):
                return True
            return False
        def dfs(r,c,visited):
            if (r<0 or c<0 or r>=rows or c>=cols or (r,c) in visited):
                return (False,False)
            visited.add((r,c)) 
            pac = pacific(r,c)  # CHANGED: track pacific reachability
            atl = atlantic(r,c)  # CHANGED: track atlantic reachability
            for dr,dc in directions:
                if (0<=r+dr<rows and 0<=c+dc<cols and heights[dr+r][c+dc] <=heights[r][c]):
                    p, a = dfs(r+dr,c+dc,visited)  # CHANGED: collect both from children
                    pac = pac or p  # CHANGED: if any path reaches pacific
                    atl = atl or a  # CHANGED: if any path reaches atlantic
                else:
                    continue
            return (pac, atl)  # CHANGED: return both reachabilities
        #MAIN FUNCTION
        for r in range(rows):
            for c in range(cols):
                pac, atl = dfs(r,c,visited)  # CHANGED: unpack tuple
                if pac and atl:  # CHANGED: only add if reaches both
                    result.append([r,c])
                visited=set()
        return result
            

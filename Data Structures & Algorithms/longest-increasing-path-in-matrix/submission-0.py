class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #dp[i][j] = from this (r,c) whats the max seq i can get
        rows,cols= len(matrix), len(matrix[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        dp=[[1]* cols for i in range(rows)]
        memo={}
        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            if (r<0 or c<0 or r>=rows or c>=cols):
                return 0 #out of bounds

            for dr,dc in directions:
                nr,nc=r+dr, c+dc
                if (nr<0 or nc<0 or nr>=rows or nc>=cols):
                    continue #out of bounds
                if matrix[r][c]<matrix[nr][nc]:
                    dp[r][c]=max(dp[r][c], 1+dfs(nr,nc))
            memo[(r,c)]= dp[r][c]
            return memo[(r,c)]
        maximum=0
        for r in range(rows):
            for c in range(cols):
                maximum=max(maximum, dfs(r,c))
        return maximum

                            
        
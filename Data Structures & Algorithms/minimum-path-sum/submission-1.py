class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        dp=[[0]*cols  for i in range(rows)]
        dp[0][0]=grid[0][0]
        for r in range(rows):
            for c in range(cols):
                if r>0 and c>0:
                    dp[r][c]=min(dp[r-1][c],dp[r][c-1])+grid[r][c]
                elif r>0:
                    dp[r][c]=dp[r-1][c]+grid[r][c]  #down moves
                elif c>0:
                    dp[r][c]=dp[r][c-1]+grid[r][c]  #right moves
        return dp[rows-1][cols-1]

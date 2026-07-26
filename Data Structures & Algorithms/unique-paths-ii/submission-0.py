class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols=len(obstacleGrid), len(obstacleGrid[0])
        dp=[[0]*cols for i in range(rows)]
        dp[0][0]=1
        for r in range(rows):
            for c in range(cols):
                #if obstacle, no way to reach
                if obstacleGrid[r][c]==1:
                    dp[r][c]=0
                    continue
                #down movement
                if r>0:
                    dp[r][c]+=dp[r-1][c]
                if c>0:
                    dp[r][c]+=dp[r][c-1]
        return dp[rows-1][cols-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DP APPROACH
        rows, cols = len(text1), len(text2)
        dp=[ [0]* (cols+1) for i in range(rows+1)]
        # we look to top left diag to return value
        # else max of top and left cells so for edge case of row 0 and col 0
        # start array of length row+1 and col+1
        for i in range(rows):
            for j in range(cols):
                if text1[i]==text2[j]:  #return result= 1+ prev subproblem
                    dp[i+1][j+1]= 1+ dp[i][j]
                else:
                    dp[i+1][j+1]=max(dp[i][j+1], dp[i+1][j])
        return dp[rows][cols]
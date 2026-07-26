class Solution:
    def numSquares(self, n: int) -> int:
        #bottoms up appraoch dp
        squares=[]
        i=1
        while i*i<=n:
            squares.append(i*i)
            i+=1
        # DP
        dp=[float('inf')]*(n+1) # dp[i] minimum no of squares required to build ith val
        dp[0]=0
        for i in range(1,n+1):
            for sq in squares:
                if sq>i:
                    continue
                dp[i]=min( dp[i], dp[i-sq]+1)
        return dp[n]
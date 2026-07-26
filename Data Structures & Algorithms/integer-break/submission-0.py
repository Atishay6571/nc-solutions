class Solution:
    def integerBreak(self, n: int) -> int:
        # remove from n in range(n) and then tackle the remaining
        # as a sub problem

        #bottoms-up
        #obj: maximize product. #dp[0]= -1 dp[1]= 0 dp[2]=1
        dp=[ i-1 for i in range((n+1))] # wherre dp[i] is max product we can get
        for i in range(2, n+1):
            for j in range(i):
                dp[i]=max(dp[i],dp[j]*(i-j),j*(i-j))
        return dp[n]

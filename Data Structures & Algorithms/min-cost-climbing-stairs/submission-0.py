class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        #at each step we make a decision
        #choose minimum cost to move forward
        cost.append(0)
        dp=[0]*(n+1)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,n+1):
            dp[i]=min(dp[i-2],dp[i-1])+cost[i]
        return dp[n]

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # given a M, player can choose anything from (1, 2M)
        # state: ( Current Index, value of M )
        # now given this state, whats the max stones they can take
        # choice: take either 1 piles or upto X piles
        # return value: the profit i get: given choice x - max(oppo) can get
        memo={}
        def dfs(i, m):
            state=(i,m)
            if state in memo:
                return memo[state]
            if (i+(2*m)-1) >= len(piles)-1:  #base case: m can take all piles
                stones=0
                while i<len(piles):
                    stones += piles[i]
                    i+=1
                memo[state]=stones
                return stones
            # take one pile at a time and increase upto X
            maxProfit=-float('inf')
            stones=0
            for x in range(2*m):
                stones+=piles[i+x]
                maxProfit=max(maxProfit, stones-dfs(i+x+1, max(x+1,m)))
            memo[state]=maxProfit
            return maxProfit
        advantage= dfs(0,1)
        return (sum(piles)+advantage)//2


            
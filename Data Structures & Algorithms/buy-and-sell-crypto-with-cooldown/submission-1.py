class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # given a decision whats the best profit you can make
        # given the remaining days
        # choices each day
        # decision --> buy sell skip
        # state : holding.   not  totalProfit as doesnt impact history
        cache={}
        def dfs(i, holding, sold_yesterday):
            if i==len(prices):
                return 0
            state=(i,holding,sold_yesterday)
            if state in cache:
                return cache[state]
            if holding: #either sell or continue holding
                cache[state]= max(dfs(i+1, False, True) + prices[i],
                        dfs(i+1, True, False)) # sell or skip
                return cache[state]
            elif not holding:
                if sold_yesterday: # can only skip as cooldown
                    cache[state] = (dfs(i+1, False, False))
                    return cache [state]
                else: # either buy or skip
                    cache[state] = max( dfs(i+1, True, False) - prices[i]
                        , dfs(i+1, False, False))
                    return cache[state]
        return dfs(0, False, False)





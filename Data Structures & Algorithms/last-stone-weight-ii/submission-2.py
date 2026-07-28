class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        '''dp(i, current_sum)
        i = which stone you're considering.
        current_sum = the sum of one partition so far.

        At each stone, you decide:
        Put it in Group A.
        Put it in Group B (or equivalently, don't put it in Group A).''' 
        memo={} #caching

        def dp(i, current_sum):
            if i==len(stones):
                return abs(current_sum)
            if (i,current_sum) in memo:
                return memo[(i,current_sum)]
            memo[(i, current_sum)]=  min(abs(dp(i+1, current_sum + stones[i])),
                            abs(dp(i+1, current_sum - stones[i])))
            return memo[i,current_sum]
        return dp(0, 0)
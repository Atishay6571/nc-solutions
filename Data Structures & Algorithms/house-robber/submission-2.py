class Solution:
    def rob(self, nums: List[int]) -> int:
        # top to bottom with memoization
        memo={} #memo[i] means max money to be looted till ith house
        def dp(i):
            #base case
            if i==0: #first house
                return nums[i]
            if i==1:
                return max(nums[i-1],nums[i])

            if i in memo:
                return memo[i]
            memo[i]=max(nums[i]+dp(i-2),dp(i-1))
            return memo[i] 
        return dp(len(nums)-1)


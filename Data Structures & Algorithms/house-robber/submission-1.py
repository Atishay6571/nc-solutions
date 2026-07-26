class Solution:
    def rob(self, nums: List[int]) -> int:
        #bottom to top
        n=len(nums)
        dp=[0]*n  # dp[i] means max money that can be stealed till ith house
        if len(nums)==1:
            return nums[0]
        dp[0]=nums[0]
        dp[1]=max(nums[1],nums[0])

        for i in range(2,n):
            dp[i]=max(nums[i]+dp[i-2], dp[i-1])
        return dp[n-1]


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dynamic programming- smaller subproblems:
        # given index i, whats the max product of subarray to left of it
        
        #bottoms up approach

        # NOTE: must track both the min and max as a number might 
        # increase if multiplied by a negative later
        n=len(nums)
        max_dp=[0]*n
        min_dp=[0]*n
        max_dp[0]=nums[0]
        min_dp[0]=nums[0]
        for i in range(1,n):
            candidates= [nums[i]*max_dp[i-1], nums[i], nums[i]*min_dp[i-1]]
            max_dp[i]=max(candidates)
            min_dp[i]=min(candidates)
        return max(max_dp)
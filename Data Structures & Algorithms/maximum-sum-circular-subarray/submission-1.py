class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        #max sum without the elements
        maximum=-float('inf')
        #start from each
        for i in range(n):
            curr_sum=0
            for j in range(i, i+n):
                curr_sum = max (nums[j%n], curr_sum+nums[j%n])
                maximum = max( maximum, curr_sum)
        return maximum

    


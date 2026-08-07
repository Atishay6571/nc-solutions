class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        result = 0 
        curr=0
        n = len(nums)
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                curr+=1
                result= max(curr,result)
            else:
                curr=0

        curr=0
        for i in range(1,n):
            if nums[i]<nums[i-1]:
                curr+=1
                result= max(curr,result)
            else:
                curr=0
        return result+1
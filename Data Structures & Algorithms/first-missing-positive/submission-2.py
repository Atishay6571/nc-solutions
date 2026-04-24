class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ##first we filter out our nums
        #key insight: missing number has to be between 1,n+1
        #CLEANING
        n=len(nums)
        for i,ele in enumerate(nums):
            if ele<=0 or ele>n+1:
                nums[i]=n+1
        
        #MARKING with Negatives
        for i in range(n):
            val=abs(nums[i])
            if 1<=val<=n:
                nums[val-1]=-abs(nums[val-1])
        #Find missing (first positive)
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        total=0
        ans=len(nums)+1
        while r<len(nums):
            if total<target:
                total+=nums[r]
                r+=1
            while total>=target:
                ans=min(ans,r-l)
                total-=nums[l]
                l+=1
                    
        if ans>len(nums):
            return 0
        return ans
        
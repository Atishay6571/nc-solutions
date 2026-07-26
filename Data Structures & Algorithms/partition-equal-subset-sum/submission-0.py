class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        part=total//2
        n=len(nums)
        # dp: top-down with memoization
        # can elements be picked in such a way to match the part sum
        def dp(i, remain):
            remain-= nums[i]
            if remain==0:
                return True
            for j in range(i+1, len(nums)):
                if dp(j,remain):
                    return True
            return False
        return dp(0,part)
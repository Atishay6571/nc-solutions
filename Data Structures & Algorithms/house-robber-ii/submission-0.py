class Solution:
    def rob(self, nums: List[int]) -> int:
    # The key insight: houses are in a circle, 
    # so house 0 and house n-1 are adjacent. You can't rob both.
    # That means either:
    # You skip house 0 → rob from houses 1 to n-1
    # You skip house n-1 → rob from houses 0 to n-2
        if len(nums)==1:
            return nums[0]
        n=len(nums)
        def rob_range(start,end):
            prev2,prev1=0,0
            for i in range(start,end):
                curr= max(prev1, prev2+nums[i])
                prev2=prev1
                prev1=curr
            return prev1
        return max(rob_range(0,n-1),rob_range(1,n))

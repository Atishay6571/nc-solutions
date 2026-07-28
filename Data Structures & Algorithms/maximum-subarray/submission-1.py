class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest=-float('inf')
        total=0
        for num in nums:
            total = max(total+num, num)
            largest=max(total,largest)

        return largest


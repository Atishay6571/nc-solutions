class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor all numbers together
        # result is your answer
        xor=0
        for i in range(len(nums)):
            xor ^= nums[i]
        return xor
            

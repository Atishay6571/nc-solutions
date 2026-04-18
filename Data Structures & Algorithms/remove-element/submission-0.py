class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        stack=[]
        while val in nums:
            nums.remove(val)
        return len(nums)
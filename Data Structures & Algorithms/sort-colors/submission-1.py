class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import defaultdict
        hmap=defaultdict(int)
        for i in nums:
            hmap[i]+=1
        overall=0
        for i in range(hmap[0]):
            nums[overall]=0
            overall+=1
        for i in range(hmap[1]):
            nums[overall]=1
            overall+=1
        for i in range(hmap[2]):
            nums[overall]=2
            overall+=1

        
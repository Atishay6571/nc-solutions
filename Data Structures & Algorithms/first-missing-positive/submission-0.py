class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        from collections import defaultdict
        minima=defaultdict(int)
        for i in nums:
            minima[i]+=1
        pos=1
        while True:
            if pos in minima:
                pos+=1
            else:
                return pos
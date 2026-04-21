class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap={}
        for i in nums:
            hmap[i]=hmap.get(i,0)+1
            if hmap[i]>=len(nums)/2:
                return i

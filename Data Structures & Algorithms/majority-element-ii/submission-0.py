class Solution:
    from collections import defaultdict
    def majorityElement(self, nums: List[int]) -> List[int]:
       size=len(nums)
       hmap=defaultdict(int)
       res=[]
       for i in nums:
        hmap[i]+=1
       for i in hmap:
        if hmap[i]>size/3:
            res.append(i)
       return res

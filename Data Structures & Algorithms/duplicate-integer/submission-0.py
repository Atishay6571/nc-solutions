class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup={}
        for i in nums:
            if i not in dup.keys():
                dup[i]=True
            else:
                return True
        return False
            
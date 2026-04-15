class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for idx, element in enumerate(nums):
            d[idx]=element
        for i in d:
            reqd= target-d[i]
            if reqd in d.values():
                for j in d:
                    if d[j]==reqd and i!=j:
                        return [i,j]





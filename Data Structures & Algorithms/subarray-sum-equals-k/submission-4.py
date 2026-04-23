class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        count=0
        prefixsums=defaultdict(int)
        presum=0
        prefixsums[0]=1
        for i in range(len(nums)):
            presum+=nums[i]
            reqd=presum-k
            if reqd in prefixsums:
                count+=prefixsums[reqd]
            prefixsums[presum]+=1

        return count
               
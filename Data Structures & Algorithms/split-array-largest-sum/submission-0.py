class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r=max(nums),sum(nums)
        res=r
        while l<r:
            splits=1
            largestSum = (l+r)//2
            subArraySum=0
            for number in nums:
                if subArraySum+number<=largestSum:
                    subArraySum+=number
                elif subArraySum+number>largestSum:
                    subArraySum=number
                    splits+=1
            if splits<=k:
                res=largestSum
                r=largestSum
            elif splits>k:
                l=largestSum+1
        return res




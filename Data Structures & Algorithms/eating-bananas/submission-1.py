class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        l,r=1,max(piles)
        res=r
        while l<=r:
            k=(l+r)//2
            totalTime=0
            for bananas in piles:
                totalTime+=ceil(bananas/k)
            if totalTime>h:
                l=k+1
            elif totalTime<=h:
                res=k
                r=k-1

        return res



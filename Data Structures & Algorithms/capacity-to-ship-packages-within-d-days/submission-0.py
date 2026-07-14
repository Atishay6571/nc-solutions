class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #leastWeightCapacity
        l,r= max(weights), sum(weights)
        while l<=r:
            capacity=(l+r)//2
            totalDays=1
            total=capacity
            for package in weights:
                if total>=package:
                    total-=package

                elif total<package:
                    totalDays+=1
                    total=capacity-package
            if totalDays>days:
                l=capacity+1
            elif totalDays<=days:
                r=capacity-1
        return l
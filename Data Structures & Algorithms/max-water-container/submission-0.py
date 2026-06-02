class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        volume=(r-l)* min(heights[r],heights[l])
        while l<r:
            if heights[l]<=heights[r]:
                l+=1
                volume=max(volume,(r-l)* min(heights[r],heights[l]))
            elif heights[l]>=heights[r]:
                r-=1
                volume=max(volume,(r-l)* min(heights[r],heights[l]))
        return volume




        
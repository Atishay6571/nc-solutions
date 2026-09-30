class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary Search for Optimal Rate
        # Rate can be between sum(piles)/hours to max(piles)
        from math import ceil
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r)//2 # rate of eating bananas
            hours_left = h
            for banana in piles:
                time_taken = ceil(banana/mid)
                hours_left -= time_taken

            if hours_left < 0:
                l = mid + 1
            else:
                r = mid # last known optimal value
        
        return r


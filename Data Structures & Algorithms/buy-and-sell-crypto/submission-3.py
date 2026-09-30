class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lptr=0
        rptr=1
        maxp=0
        while rptr<len(prices):
            profit=prices[rptr]-prices[lptr]
            if profit>0:
                maxp=max(maxp,profit)
            else:
                lptr=rptr
            rptr+=1
        return maxp



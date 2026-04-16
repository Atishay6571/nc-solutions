class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits=[0]
        for idx, ele in enumerate(prices):
            for j in range(idx+1,len(prices)):
                profit= prices[j]-ele
                profits.append(profit)
        return max(profits)
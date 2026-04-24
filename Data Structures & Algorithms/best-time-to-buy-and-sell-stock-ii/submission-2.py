class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        from collections import defaultdict

        profits=0
        sell=0
        check=0
        for i in range(len(prices)-1):

            if prices[i+1]<prices[i]:
                sell=prices[i]
                if i!=0:
                    profits+=(sell-buy)
                buy=prices[i+1]
                check+=1

            else:
                if i==0:
                    buy=prices[0]
                if i==len(prices)-2:
                    profits+=prices[len(prices)-1]-buy
        if check==0:
            return prices[-1]-prices[0]    
        return profits


            
        
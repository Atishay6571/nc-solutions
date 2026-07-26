class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={} # has amounts
        def dp(amount):
            if amount==0:
                return 0
            if amount in memo:
                return memo[amount]
            minimum=float('inf')
            for coin in coins:
                remaining= amount-coin
                if remaining<0:
                    continue
                minimum = min(minimum, 1+dp(remaining))
            memo[amount]=minimum
            return minimum
        value= dp(amount)
        if value == float('inf'):
            return -1
        return value
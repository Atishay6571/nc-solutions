class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            best = float('-inf')
            stones_taken = 0
            for take in range(1, 4):
                if i + take - 1 >= n:
                    break
                stones_taken += stoneValue[i + take - 1]
                best = max(best, stones_taken - dp[i + take])
            dp[i] = best
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"        
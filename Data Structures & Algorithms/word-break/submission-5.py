class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom - up approach
        # dp[i] - can we reach ith index using valid words
        dp = [ 0 for i in range(len(s) + 1) ]
        dp[0] = 1
        # for each end, we loop over all possible valid starts till now
        for end in range(len(s)+1):
            for start in range(end):
                if dp[start]==1 and s[start:end] in wordDict:
                    dp[end] = 1
                    break
        return True if (dp[len(s)]) == 1 else False


            
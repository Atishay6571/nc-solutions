class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp: after a valid word in found, run dp on new substring
        # top-down approach with memoization
        memo={}
        def dp(i):   # i : current index of string we are at
            if i==len(s):
                return True
            if i in memo:
                return memo[i]
            end=i
            while end<len(s):
                if s[i:end+1] in wordDict:
                    if dp(end+1):
                        memo[i]=True
                        return True
                end+=1
            memo[i]=False
            return False
                    
        return dp(0)


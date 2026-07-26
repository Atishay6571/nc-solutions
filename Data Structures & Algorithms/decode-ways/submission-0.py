class Solution:
    def numDecodings(self, s: str) -> int:
        # top down approach -DP with memoization
        # at each choice, either choose i or i-1 and solve the rest
        memo={}
        def isValid(num):
            length=len(num)
            num=int(num)
            if 0<num<=26:
                if 0<num<=9 and length==2:
                    return False
                return True
            return False
        def dp(s):
            if len(s)==0:
                return 1
            if len(s)==1:
                if isValid(s):
                    return 1
                return 0
            if s in memo:
                return memo[s]
            memo[s]=0
            if isValid(s[-1]):
                memo[s]+= dp(s[:-1:])
            if isValid(s[-2::]):
                memo[s]+= dp(s[:-2:])
            return memo[s]
        return dp(s)
            

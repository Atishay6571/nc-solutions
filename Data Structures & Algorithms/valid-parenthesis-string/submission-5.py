class Solution:
    def checkValidString(self, s: str) -> bool:
        lo,hi=0,0 # minimum and maximum possible open parentheses
        for char in s:
            if char=="(":
                lo+=1
                hi+=1
            elif char==")":
                lo-=1
                hi-=1
            elif char=="*":
                lo-=1
                hi+=1
            if hi < 0:
                return False   # too many ')' even using all '*' as '('
            lo = max(lo, 0)    # can't have negative open parens
        return lo == 0
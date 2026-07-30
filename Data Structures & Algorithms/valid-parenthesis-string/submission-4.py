class Solution:
    def checkValidString(self, s):
        lo = 0   # minimum possible open parens
        hi = 0   # maximum possible open parens
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:  # '*'
                lo -= 1   # * could be ')'
                hi += 1   # * could be '('
            if hi < 0:
                return False   # too many ')' even using all '*' as '('
            lo = max(lo, 0)    # can't have negative open parens
        return lo == 0
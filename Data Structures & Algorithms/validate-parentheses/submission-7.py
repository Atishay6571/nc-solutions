class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {')':'(', '}':'{',']':'['}
        stack = []
        for ch in s:
            if ch in ['(','{','[']:
                stack.append(ch)
            else:
                if not stack or stack[-1] != hmap[ch]:
                    return False
                if stack:
                    stack.pop()
        return True if len(stack) == 0 else False


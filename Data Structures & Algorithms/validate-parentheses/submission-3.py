class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch in ["{","[","("]:
                stack.append(ch)
            else:
                if len(stack)>0:
                    last=stack.pop()
                    if last=="{" and ch!="}":
                        return False
                    elif last=="(" and ch!=")":
                        return False
                    elif last=="[" and ch!="]":
                        return False
                else:
                    return False
        else:
            if len(stack) >0:
                return False
            return True

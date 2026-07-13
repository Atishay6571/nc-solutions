class Solution:
    def decodeString(self, s: str) -> str:
        curr=""
        number=[]
        stack=[]
        numbs=""
        Numberflag=False
        for i in s:
            if i=="[":
                number.append(int(numbs))
                numbs=""
                stack.append(curr)
                curr=""
            elif i=="]":
                num=number.pop()
                curr=stack.pop()+(num*curr)

            elif i.isalpha():
                curr+=i

            elif i.isnumeric():
                numbs+=i
        return curr
            
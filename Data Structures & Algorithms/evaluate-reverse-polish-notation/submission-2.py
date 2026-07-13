class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for token in tokens:
            if token not in {"+","-","/","*"}:
                stack.append(token)
            else:
                b=int(stack.pop())
                a=int(stack.pop())
                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                elif token == "/":
                    result = int(a / b)
                stack.append(result)
        return int(stack.pop())
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result=[]
        if digits=="":
            return result
        def dfs(digitIndex,current):
            if len(current)==len(digits):
                result.append("".join(current))
            if digitIndex<len(digits):
                digit=digits[digitIndex]
            else:
                return
            for i in range(len(mapping[digit])):
                current.append(mapping[digit][i])
                dfs(digitIndex+1,current)
                current.pop()
        dfs(0,[])
        return result


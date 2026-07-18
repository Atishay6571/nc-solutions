class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        def backtracking(start,current):
            if len(s)==start:
                result.append(current.copy())
                return
            for end in range(start+1,len(s)+1):
                substring=s[start:end]
                if substring[::]==substring[::-1]:
                    current.append(substring)
                    backtracking(end,current)
                    current.pop()
        backtracking(0,[])
        return result
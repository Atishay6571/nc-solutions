class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result=[]
        part=[]
        def backtracking(start):
            if start == len(s):
                result.append(" ".join(part))
                return 
                #return the answer
            for end in range(start, len(s)):
                if (end<len(s)+1 and s[start:end+1] in wordDict):
                    part.append(s[start:end+1])
                    backtracking(end+1) #recurse for next words
                    part.pop() #incase more words exist with same start

        backtracking(0)
        return result



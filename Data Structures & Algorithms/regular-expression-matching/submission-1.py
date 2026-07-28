class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #dfs(i,j) mean can s[i:] be matched to p[j:]
        def dfs(i,j):
            if j>=len(p):
                return i>=len(s)
            #handle ".*" as a unit
            if j<len(p)-1 and p[j+1]=="*":
                if i<len(s) and p[j] in [s[i],"."]:
                    # skip the pair, keep the pair and move
                    return dfs(i,j+2) or dfs(i+1,j) 
                return dfs(i,j+2) 
            else:
                if i<len(s) and p[j] in [ s[i], "."]:
                    return dfs(i+1, j+1)
            return False

        return dfs(0,0)

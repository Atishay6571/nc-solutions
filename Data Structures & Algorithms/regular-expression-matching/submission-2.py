class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #dfs(i,j) mean can s[i:] be matched to p[j:]
        memo={}#memo
        def dfs(i,j):
            state=(i,j)
            if state in memo:
                return memo[state]
            if j>=len(p):
                memo[state]= (i>=len(s))
                return memo[state]
            #handle ".*" as a unit
            if j<len(p)-1 and p[j+1]=="*":
                if i<len(s) and p[j] in [s[i],"."]:
                    # skip the pair, keep the pair and move
                    memo[state]= dfs(i,j+2) or dfs(i+1,j) 
                    return memo[state]
                memo[state] = dfs(i,j+2) 
                return memo[state]
            else:
                if i<len(s) and p[j] in [ s[i], "."]:
                    memo[state] = dfs(i+1, j+1)
                    return memo[state]
            memo[state]=False
            return False

        return dfs(0,0)

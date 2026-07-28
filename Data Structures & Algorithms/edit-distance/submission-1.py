class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dfs(i,j) specifies minimum changes required to match
        # state: dfs[i:]and dfs[j:]
        # returns min number of combinations to match
        memo={}
        def dfs(i,j):
            state=(i,j)
            if state in memo:
                return memo[state]
            if i==len(word1) or j==len(word2):
                memo[state] = (len(word1)-i)+(len(word2)-j)
                return memo[state]
            if word1[i]==word2[j]:
                memo[state] = dfs(i+1, j+1)
                return memo[state]
            else: #if doesnt match then 3 options: skip, delete, insert
                memo[state] = min(dfs(i+1,j+1), dfs(i+1,j), dfs(i,j+1))+1
                return memo[state]
        return dfs(0,0)
        


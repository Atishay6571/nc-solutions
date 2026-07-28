class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #dp: given index(i,j) for s,t how many ways to build from s[i] and t[j]
        # state at each given (i,j)
        # choice at each state: take in subsequence or skip
        # return number of unique subsequences
        cache={}
        def dfs(i,j):
            state=(i,j)
            if state in cache:
                return cache[state]
            #base cases
            if j==len(t): #found a subseq
                cache[state]=1
                return 1
            elif i==len(s):
                cache[state]=0
                return 0
            if s[i]==t[j]:
                cache[state]= dfs(i+1,j+1)+ dfs(i+1,j)
                return cache[state]
            else:
                cache[state] = dfs(i+1,j)
                return cache[state]
        return dfs(0,0)
            

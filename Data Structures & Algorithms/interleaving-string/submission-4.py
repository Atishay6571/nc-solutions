class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp: index1 for s1, index2 for s2
        # state: given current index of s3, can we build s3 from i1, i2
        # decisiom: continue with same substring or switch 
        memo={} # add caching
        def dfs(i1, i2):   #i3 can be calculatd from i1+i2
            state=(i1,i2)
            if state in memo:
                return memo[state]
            if i1==len(s1) and i2==len(s2):
                if i1+i2==len(s3):
                    return True
                else:
                    return False
            elif i1==len(s1):
                if s2[i2]==s3[i1+i2]:
                    memo[state]= dfs(i1, i2+1)
                    return memo[state]
                else:
                    return False
            elif i2==len(s2):
                if s1[i1]==s3[i1+i2]:
                    memo[state]= dfs(i1+1, i2)
                    return memo[state]
                else:
                    return False

            if s1[i1]==s3[i1+i2] and s2[i2]==s3[i1+i2]:
                memo[state]= dfs(i1+1,i2) or dfs(i1,i2+1)
                return memo[state]

            elif s1[i1]==s3[i1+i2]:
                memo[state]= dfs(i1+1, i2)
                return memo[state]

            elif s2[i2]==s3[i1+i2]:
                memo[state]= dfs(i1,i2+1)
                return memo[state]

            else:
                return False
        if len(s1)+len(s2)!= len(s3):
            return False
        return dfs(0,0)
            

            
class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        #odd length
        for i in range(len(s)):
            l,r=i,i
            while (l>=0 and r<len(s) and s[l]==s[r]):
                count+=1
                r+=1
                l-=1
        #even length
        for i in range(len(s)-1):
            l,r=i,i+1
            while (l>=0 and r<len(s) and s[l]==s[r]):
                count+=1
                r+=1
                l-=1
        return count

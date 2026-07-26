class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=0
        #approach: consider each index as center and expand outwards
        length=0
        string=""
        #odd length
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if length < r-l+1:
                    length=r-l+1
                    string=s[l:r+1]
                r+=1
                l-=1
            
        #even length
        for i in range(len(s)-1):
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if length < r-l+1:
                    length=r-l+1
                    string=s[l:r+1]
                r+=1
                l-=1
        return string
        

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        ans=1
        visited=set()
        if len(s)==0:
            return 0     
        visited.add(s[0])   
        while l<=r and r<len(s)-1:

            if s[r+1] not in visited:
                visited.add(s[r+1])
                r+=1
                ans=max(ans,r-l+1)
            else:
                while s[r+1] in visited:
                    visited.remove(s[l])
                    l+=1
                visited.add(s[r+1])
                r+=1


        return ans
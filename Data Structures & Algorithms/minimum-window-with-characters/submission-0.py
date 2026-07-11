class Solution:
    from collections import defaultdict
    def minWindow(self, s: str, t: str) -> str:
        d= defaultdict(int)
        for element in t:
            d[element]+=1
        l=0
        r=0
        have=0
        need=len(d)
        low=len(s)+1
        stri=""
        current=defaultdict(int)
        for r in range(len(s)):
            current[s[r]]+=1
            if d[s[r]]==current[s[r]]:
                have+=1
            while have==need:
                if low>r-l+1:
                    low=min(low,r-l+1)
                    stri=s[l:r+1]
                if d[s[l]]==current[s[l]]:
                    have-=1
                current[s[l]]-=1
                l+=1
        return stri



         
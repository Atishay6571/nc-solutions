class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        hmap=defaultdict(int)
        if len(s)==0:
            return 0
        result=0
        while l<=r and r<len(s):
            hmap[s[r]]+=1
            if r-l+1-max(hmap.values())<=k:
                result=max(result,r-l+1)
                r+=1
                
            else:
                while (r-l+1)-max(hmap.values())>k:
                    hmap[s[l]]-=1
                    l+=1
                r+=1
        return result
        
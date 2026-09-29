class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # record last known index of each char
        n = len(s)
        hmap = {}
        curr = 0
        best = 0
        start = 0
        for i in range(n):
            if s[i] not in hmap:
                curr += 1
                
            else:
                start = max(start, hmap[s[i]]+1)
                curr = i - start + 1
            
            hmap[s[i]] = i
            best = max( best, curr)
        return best
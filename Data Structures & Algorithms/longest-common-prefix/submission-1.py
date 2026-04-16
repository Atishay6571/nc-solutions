class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        mini=min(strs)
        low=len(mini)
        for i in range(low):
            for j in range(len(strs)-1):
                if strs[j][i]!=strs[j+1][i]:
                    return ans
            ans+=strs[0][i]
        return ans

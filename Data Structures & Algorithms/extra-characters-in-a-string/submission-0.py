class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        class TrieNode:
            def __init__(self):
                self.isEnd = False
                self.children = {}

        # Build Trie
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.isEnd = True

        # DFS + Memoization
        dp = {len(s): 0}  # base case: no characters left = 0 extras

        def dfs(i):
            if i in dp:
                return dp[i]

            res = 1 + dfs(i + 1)  # option 1: skip s[i], it's extra

            curr = root             # option 2: try matching words from position i
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.isEnd:      # found a complete word s[i:j+1]
                    res = min(res, dfs(j + 1))

            dp[i] = res
            return res

        return dfs(0)
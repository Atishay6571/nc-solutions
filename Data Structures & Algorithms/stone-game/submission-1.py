class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dynamic programming
        # choice: (take start, take last)
        # state: (start index, last index)
        # returns max profit other person can get
        memo={}
        def dfs(start, end):
            state=(start,end)
            if state in memo:
                return memo[state]
            if start==end: #base case
                memo[state]=piles[start]
                return piles[start]
            #make a choice:
            # my profit is current choice- max the person can make from remaining
            memo[state]= max(piles[start]-dfs(start+1, end),
                        piles[end]- dfs(start, end-1))
            return memo[state]

        if dfs(0, len(piles)-1) >0:
            return True
        else:
            return False
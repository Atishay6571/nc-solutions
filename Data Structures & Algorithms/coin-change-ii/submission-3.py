class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp: given a choice of coin, can we make remaining
        # if yes way+=1
        cache={}
        def dfs(amount, start):  #index corresponds to coins already used to prevent permutations
            #base case
            if amount==0:
                return 1
            elif amount <0:
                return 0
            state=(amount,start)
            if state in cache:
                return cache[state]
            combinations=0
            for i in range(start, len(coins)):
                remain=amount-coins[i]
                combinations+= dfs(remain,i)
            cache[state]=combinations
            return combinations
        return dfs(amount,0)            
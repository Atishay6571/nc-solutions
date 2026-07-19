class Solution:
    def makesquare(self, matchsticks):
        if sum(matchsticks) % 4 != 0:
            return False
        target = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)  # big first, prune faster
        sides = [0, 0, 0, 0]

        def backtrack(idx):
            if idx == len(matchsticks):
                return True  # all matchsticks placed
            for i in range(4):
                if sides[i] + matchsticks[idx] <= target:
                    sides[i] += matchsticks[idx]       # choose
                    if backtrack(idx + 1):              # explore
                        return True
                    sides[i] -= matchsticks[idx]       # unchoose
                # prune: skip duplicate sides
                if sides[i] == 0:
                    break
            return False

        return backtrack(0)
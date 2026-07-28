class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp: at each state: choose +ve or -ve
        # given the choice: subproblem is target -= choice
        def dfs(index,left):
            #last index and target met
            if index==len(nums):
                if left==0:
                    return 1
                else:
                    return 0
            return dfs(index+1, left +nums[index])+dfs(index+1, left-nums[index])
        return dfs(0, target)

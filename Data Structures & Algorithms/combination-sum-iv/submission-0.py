class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp: given a target, how many ways it can be reached
        # sub problem, remove an element and check if that new target 
        # is reachable
        # TOP- DOWN APPROACH
        n=len(nums)
        memo={} # for a given target, how many ways to reach it
        def dp(req):
            if req==0: #base case if no req is there
                return 1
            if req in memo:
                return memo[req]
            if req<0:
                return 0
            total=0
            for i in range(n):
                total+=dp(req-nums[i])
            memo[req]=total
            return total
        return dp(target)
                
            
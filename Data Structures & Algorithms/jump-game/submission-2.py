class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # approach: what's the farthest I can reach?
        farthest=0 #farthest reachable index
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest= max(farthest, nums[i]+i)
        return True
        
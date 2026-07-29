class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps=0
        farthest=0  # farthest possible to go from here
        current_end = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, nums[i]+i)
            if current_end==i:
                jumps+=1
                current_end=farthest
        return jumps

            

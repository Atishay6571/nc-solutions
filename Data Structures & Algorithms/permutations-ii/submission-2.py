class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        permutations = []
        used = [False] * len(nums)
        
        def backtracking(current):
            if len(current) == len(nums):
                permutations.append(current.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                current.append(nums[i])
                backtracking(current)
                current.pop()
                used[i] = False
        
        backtracking([])
        return permutations
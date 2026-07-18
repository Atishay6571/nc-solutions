class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations=[]
        def backtracking(current):
            for i in range(0,len(nums)):
                if current and nums[i] in current:
                    continue
                current.append(nums[i])
                if len(current)==len(nums):
                    permutations.append(current.copy())
                else:
                    backtracking(current)
                current.pop()
        backtracking([])
        return permutations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[[]]
        def backtracking(start,current):
            for i in range(start,len(nums)):
                current.append(nums[i])
                result.append(current.copy())
                backtracking(i+1,current)
                current.pop()
        backtracking(0,[])
        return result
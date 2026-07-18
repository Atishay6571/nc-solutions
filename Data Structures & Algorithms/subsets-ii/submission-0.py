class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets2=[[]]
        nums.sort()
        def backtracking(start,current):
            for i in range(start,len(nums)):
                #check for duplicates
                if i>start and nums[i]==nums[i-1]:
                    continue
                current.append(nums[i])
                subsets2.append(current.copy())
                backtracking(i+1,current)
                current.pop()
        backtracking(0,[])
        return subsets2

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #keep searching and expanding till u find sol
        results=[]
        def backtrack(start,current):
            for i in range(start,len(nums)):
                current.append(nums[i])
                if sum(current)==target:
                    results.append(current.copy())
                elif sum(current)<target:
                    backtrack(i,current)                    
                current.pop()
        backtrack(0,[])
        return results

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def backtracking(start, current):
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # skip duplicate at same level
                current.append(candidates[i])
                if target > sum(current):
                    backtracking(i + 1, current)
                elif target == sum(current):
                    result.append(current.copy())
                current.pop()
        backtracking(0,[])
        return result
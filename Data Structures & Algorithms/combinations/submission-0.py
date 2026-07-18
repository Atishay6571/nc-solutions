class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combination=[]
        def backtracking(start,current):
            for i in range(start,n+1):
                current.append(i)
                if len(current)==k:
                    combination.append(current.copy())
                elif len(current)<k:
                    backtracking(i+1,current)
                current.pop()
        backtracking(1,[])
        return combination
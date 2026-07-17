class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        results=[]
        def backtracking(start,current):
            for i in range(start,len(nums)):
                current.append(nums[i])
                results.append(current.copy())
                backtracking(i+1,current)
                current.pop()        
        backtracking(0,[])
        xorResults=0
        for subset in results:
            xor=0
            for number in subset:
                xor^=number
            xorResults+=xor
        return xorResults

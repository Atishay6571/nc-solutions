class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        #Divisibility is transitive. If a | b and b | c, then a | c.
        nums.sort()

        best=[]
        cache ={}
        def dp(index):
            # skip divisible number or take and moeve on 
            if index in cache:
                return cache[index]
            temp = []
            for i in range(index+1, len(nums)):
                if nums[i]%nums[index]==0:
                    candidate = dp(i)
                    if len(candidate)>len(temp):
                        temp = candidate
            cache[index] = [nums[index]]+temp
            return cache[index]
        
        for i in range(len(nums)):
            val = dp(i)
            if len(val)>len(best):
                best= val
        return best

                    
                


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hmap={}
        prod=1
        special=0
        for idx,val in enumerate(nums):
            if val==0:
                special+=1
                if special>=2:
                    return [0]*len(nums)
                continue
            prod*=val
        output=[]
        if special==1:
            for i in nums:
                if i==0:
                    output.append(prod)
                else:
                    output.append(0)
            return output
        for i in nums:
            output.append(prod//i)
        return output

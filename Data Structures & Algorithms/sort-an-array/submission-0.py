class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        left=self.sortArray(nums[:len(nums)//2])
        right=self.sortArray(nums[len(nums)//2:])
        return self.merge(left,right)
    def merge(self,left,right):
        res=[]
        i=0
        lptr=0
        rptr=0
        while lptr<len(left) and rptr<len(right):
            if left[lptr]<right[rptr]:
                res.append(left[lptr])
                lptr+=1
            else:
                res.append(right[rptr])
                rptr+=1
        while lptr<len(left):
            res.append(left[lptr])
            lptr+=1
        while rptr<len(right):
            res.append(right[rptr])
            rptr+=1
        return res


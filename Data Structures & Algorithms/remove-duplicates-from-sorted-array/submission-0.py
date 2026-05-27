class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt=0
        for i in range(len(nums)-1):
                if nums[i]!=nums[i+1]:
                    nums[cnt]=nums[i]
                    cnt+=1
        nums[cnt]=nums[-1]
        cnt+=1
        return cnt
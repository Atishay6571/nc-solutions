class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # index must be odd and even, if not then lone wolf found
        l, r = 0, len(nums)-1
        if len(nums)==1:
            return nums[0]
        while l <= r:
            mid = (l+r)//2
            leftSame = mid>0 and nums[mid]==nums[mid-1] 
            rightSame =  mid+1 < len(nums) and nums[mid] == nums[mid+1]
            if not leftSame and not rightSame:
                return nums[mid]
            if rightSame:
                if mid%2 == 0:
                    l = mid+2
                elif mid% 2 !=0:
                    r= mid-1
            elif leftSame:
                if mid%2 == 0:
                    r=mid-1
                elif mid%2!=0:
                    l=mid+1
        
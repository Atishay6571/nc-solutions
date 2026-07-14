class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r=0,len(nums)-1

        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return True
            ###this is the new logic here!
            if nums[mid] == nums[l] == nums[r]:
                l += 1
                r -= 1
                continue
            ######


            if nums[mid]<=nums[r]:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            elif nums[mid]>=nums[l]:
                if nums[mid]>target>=nums[l]:
                    r=mid-1
                else:
                    l=mid+1

        return False
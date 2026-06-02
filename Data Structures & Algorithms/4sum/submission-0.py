class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                reqd=target-nums[i]-nums[j]
                l=j+1
                r=len(nums)-1
                while l<r:
                    if nums[l]+nums[r]<reqd:
                        l+=1
                    elif nums[l]+nums[r]>reqd:
                        r-=1
                    else:
                        ans.add(tuple([nums[i],nums[j],nums[l],nums[r]]))
                        l+=1
                        r-=1
        return list(ans)



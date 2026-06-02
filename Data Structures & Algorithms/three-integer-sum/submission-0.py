class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer=[]
        for i in range(len(nums)-2):
            target=-nums[i]
            r=len(nums)-1
            l=i+1

            while l<r:
                if nums[l]+nums[r]<target:
                    l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    if [nums[l],nums[r],nums[i]] not in answer:
                        answer.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1
        return answer

                

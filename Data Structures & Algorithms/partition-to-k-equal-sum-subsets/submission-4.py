class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False
        requirement=sum(nums)//k
        array=[0]*k
        nums.sort(reverse=True)
        def backtrack(index):
            if index==len(nums):
                return True
            for i in range(k):
                if array[i]+nums[index]<=requirement:
                    array[i]+=nums[index]
                    if backtrack(index+1):
                        return True
                    array[i]-=nums[index]
                    if array[i]==0:
                        break

                else:
                    continue
            return False

        return backtrack(0)



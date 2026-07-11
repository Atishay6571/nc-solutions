class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        left=0
        right=k-1
        answer=[]
        hmap=defaultdict(int)
        maximum=0
        for i in range(k):
            hmap[nums[i]]+=1
            
        for i in range(k-1,len(nums)):
            answer.append(max(hmap.keys()))
            hmap[nums[left]]-=1
            if hmap[nums[left]]==0:
                hmap.pop(nums[left])
            left+=1
            if (right+1)!=len(nums):
                right+=1
                hmap[nums[right]]+=1
        return answer
            
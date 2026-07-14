class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]     # one step from meeting point
            slow2 = nums[slow2]   # one step from start
            if slow == slow2:
                return slow

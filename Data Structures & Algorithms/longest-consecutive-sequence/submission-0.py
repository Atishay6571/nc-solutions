class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0
        for num in numSet:
            if num-1 not in numSet:
                series=num
                length=0
                while series in numSet:
                    length+=1
                    series+=1
                longest=max(longest,length)
        return longest


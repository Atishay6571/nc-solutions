class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ptr1=0
        ptr2=0
        merged=[]
        while ptr1<len(nums1) and ptr2<len(nums2):
            if nums1[ptr1]>nums2[ptr2]:
                merged.append(nums2[ptr2])
                ptr2+=1
            elif nums1[ptr1]<=nums2[ptr2]:
                merged.append(nums1[ptr1])
                ptr1+=1
        while ptr1<len(nums1):
            merged.append(nums1[ptr1])
            ptr1+=1
        while ptr2<len(nums2):
            merged.append(nums2[ptr2])
            ptr2+=1
        if len(merged)%2!=0:
            return merged[len(merged)//2]
        else:
            return ((merged[len(merged)//2])+(merged[((len(merged))//2)-1]))/2
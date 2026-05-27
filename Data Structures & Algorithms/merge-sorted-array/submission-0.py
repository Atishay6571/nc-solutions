class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        test=[]
        nums1ptr=0
        nums2ptr=0
        while nums1ptr<len(nums1)-len(nums2) and nums2ptr<len(nums2):
            if nums1[nums1ptr]<=nums2[nums2ptr]:
                test.append(nums1[nums1ptr])
                nums1ptr+=1
            else:
                test.append(nums2[nums2ptr])
                nums2ptr+=1
        while nums1ptr<len(nums1)-len(nums2):
            test.append(nums1[nums1ptr])
            nums1ptr+=1
        while nums2ptr<len(nums2):
            test.append(nums2[nums2ptr])
            nums2ptr+=1
        for i,ele in enumerate(test):
            nums1[i]=ele
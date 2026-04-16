class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap={}
        for idx,ele in enumerate(nums):
            if ele not in hmap:
                hmap[ele]=idx
            else:
                dist=idx-hmap[ele]
                if dist<=k:
                    return True
                hmap[ele]=idx
        return False
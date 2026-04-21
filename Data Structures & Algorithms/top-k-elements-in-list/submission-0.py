class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        for i in nums:
            hmap[i]=hmap.get(i,0)+1
        res=[]
        for i in range(k): 
            highv=0
            highk=0
            for key,val in hmap.items():
                if val>highv:
                    highv=val
                    highk=key
            res.append(highk)
            hmap.pop(highk)
        return res



class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        heapq.heapify(self.nums) # NOTE: this returns None so dont return
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)
    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        

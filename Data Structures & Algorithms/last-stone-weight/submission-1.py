class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #MAX-HEAP- idea is to pop 2 max elements and add result
        #Note: MAX HEAP IS NOT DEFAULT
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1==stone2:
                continue
            else:
                heapq.heappush(stones, stone1-stone2)
        return -stones[0] if len(stones)>0 else 0
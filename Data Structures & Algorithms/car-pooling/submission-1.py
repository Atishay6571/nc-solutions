class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        current=0
        heap=[] #drop,passengers
        trips.sort(key=lambda x: x[1])
        for passengers, pick, drop in trips:
            while heap and heap[0][0]<=pick:
                current-=heapq.heappop(heap)[1]
            current+=passengers
            heapq.heappush(heap,[drop,passengers])
            if current>capacity:
                return False
        return True
        
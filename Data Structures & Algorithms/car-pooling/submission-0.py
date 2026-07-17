class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        overlap=[0]*1000
        for trip in trips:
            for i in range(trip[1],trip[2]):
                overlap[i]+=trip[0]
                if overlap[i]>capacity:
                    return False
        return True
        
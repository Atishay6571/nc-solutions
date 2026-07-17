class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from math import sqrt
        points=[[sqrt((x**2) + (y**2)),x,y] for x,y in points]
        result=[]
        heapq.heapify(points)
        for i in range(k):
            point=heapq.heappop(points)
            result.append([point[1],point[2]])
        return result
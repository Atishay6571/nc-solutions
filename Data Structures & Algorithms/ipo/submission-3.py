class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #need to look at all projects available in the current capital
        #use a MIN HEAP

        capital=[[capital[project],project] for project in range(len(capital))]
        heapq.heapify(capital)
        totalProfits=[]
        heapq.heapify(totalProfits)

        for i in range(k):
            while capital and capital[0][0]<=w:
                element=heapq.heappop(capital)
                project=element[1]
                heapq.heappush(totalProfits,-profits[project])

            if totalProfits==[]:
                return w
            #then choose the maximum profit among those
            #use a MAX HEAP

            gain=-heapq.heappop(totalProfits)
            w+=gain
        return w


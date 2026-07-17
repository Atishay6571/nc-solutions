class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #need to look at all projects available in the current capital
        #use a MIN HEAP

        capital=[[capital[project],project] for project in range(len(capital))]
        heapq.heapify(capital)
        totalProfits=[]
        for i in range(k):
            while capital and capital[0][0]<=w:
                element=heapq.heappop(capital)
                project=element[1]
                totalProfits.append([-profits[project],project])

            if totalProfits==[]:
                return w
            #then choose the maximum profit among those
            #use a MAX HEAP

            heapq.heapify(totalProfits)
            gain=-heapq.heappop(totalProfits)[0]
            w+=gain
        return w


class MedianFinder:

    def __init__(self):
        #idea being maintain 2 small heaps for large and small
        self.small=[] #max heap
        self.large=[] #min heap
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        if len(self.small)==len(self.large):
            if len(self.small)==0:
                heapq.heappush(self.small,-num)
                return
            if abs(-self.small[0])<num< self.large[0]:
                heapq.heappush(self.large,num)
            elif abs(-self.small[0])>num:
                heapq.heappush(self.small,-num)
            else:
                heapq.heappush(self.large,num)
        elif abs(len(self.small)-len(self.large))==1:
            if len(self.large)==0:
                if num<-self.small[0]:
                    heapq.heappush(self.large,-heapq.heappop(self.small))
                    heapq.heappush(self.small,-num)
                else:
                    heapq.heappush(self.large,num)
                return
            if abs(-self.small[0])<num< self.large[0]:
                if len(self.small)>len(self.large):
                    heapq.heappush(self.large,num)
                else:
                    heapq.heappush(self.small,-num)
            elif abs(-self.small[0])>num:
                if len(self.small)>len(self.large):
                    heapq.heappush(self.large,-heapq.heappop(self.small))
                heapq.heappush(self.small,-num)
            else:
                if len(self.large)>len(self.small):
                    heapq.heappush(self.small,-heapq.heappop(self.large))
                heapq.heappush(self.large,num)

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -self.small[0]
        elif len(self.small)<len(self.large):
            return self.large[0]
        else:
            return (self.large[0]-self.small[0])/2
        
        
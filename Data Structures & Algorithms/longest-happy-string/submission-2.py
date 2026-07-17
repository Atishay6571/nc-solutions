class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap=[]
        result=""
        if a>0:
            heap.append([-a,'a'])
        if b>0:
            heap.append([-b,'b'])
        if c>0:
            heap.append([-c,'c'])
        heapq.heapify(heap)
        while heap:
            element=heapq.heappop(heap)
            if len(result)>1:
                if element[1]!=result[-1] or element[1]!=result[-2]:
                    result+=element[1]
                    element[0]+=1
                    if element[0]<0:
                        heapq.heappush(heap,element)
                else:
                    if heap:
                        new=heapq.heappop(heap)
                        heapq.heappush(heap,element)
                        element=new
                        result+=element[1]
                        element[0]+=1
                        if element[0]<0:
                            heapq.heappush(heap,element)                       
                    else:
                        break
            else:
                result+=element[1]
                element[0]+=1
                if element[0]<0:
                    heapq.heappush(heap,element) 
        return result 
                    

        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import deque
        time=0 #time-elapsed
        queue=deque() # to store elements under cooldown with their time
        counts=[0]*26
        for task in tasks:
            counts[ord(task)-ord("A")]+=1
        #Note: we dont need to track which letter is which as it asks for count
        #MAX_HEAP: to store tasks of non-zero freq
        heap=[]
        counts=[-s for s in counts]
        for count in counts:
            #while pushing to heap, keep format of heap same
            if count!=0:
                heapq.heappush(heap,[count,0])
        #Now heap is ready: pop element and add them into waiting queue
        while heap or queue:
            time+=1
        #queue would have structure like [freq remaining, time at which its freed]    
            if queue:              
                if queue[0][1]<=time:
                    element=queue.popleft()
                    heapq.heappush(heap,element)

            if len(heap)>0:
                task=heapq.heappop(heap) 
                if task[0]<-1:
                    queue.append([task[0]+1,time+n+1])
        return time
            
class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import deque
        #Queue for cooldown period
        time=0
        result=""
        queue=deque()
        chars=[0]*26
        for character in s:
            chars[ord(character)-ord('a')]+=1
        # Max Heap to use the maximum frequency
        heap=[[-chars[i],chr(i+ord('a')),0] for i in range(len(chars)) if chars[i]!=0]

        heapq.heapify(heap)
        while heap or queue:
            time+=1
            #queue first
            if queue:
                if queue[0][2]<=time:
                    heapq.heappush(heap,queue.popleft())

            #now heap
            if heap:
                character=heapq.heappop(heap)
                result+=character[1]
                if character[0]<-1:
                    queue.append([character[0]+1,character[1],time+2])
                else:
                    continue
            else:
                result=""
                break
        return result


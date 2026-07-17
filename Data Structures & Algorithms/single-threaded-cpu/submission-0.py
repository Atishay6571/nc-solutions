class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #min heap for least processing time
        #min heap for least enque time
        tasks=[[tasks[i][0],tasks[i][1],i] for i in range(len(tasks))]
        heapq.heapify(tasks)
        time=1
        result=[]
        while tasks:
            task=tasks[0]
            if task[0]>time:
                time=task[0]
                heapq.heappop(tasks)
            elif task[0]<=time:
                #multiple tasks available now! which to pick?
                heap=[]
                while tasks and tasks[0][0]<=time:
                    heap.append(heapq.heappop(tasks))
                heap=[[heap[i][1],heap[i][2]] for i in range(len(heap))]
                heapq.heapify(heap)
                task=heapq.heappop(heap)
                task=[time,task[0],task[1]]
                while heap:
                    leftOver=heapq.heappop(heap)
                    leftOver=[time,leftOver[0],leftOver[1]]
                    heapq.heappush(tasks,leftOver)
                    

            result.append(task[2])
            time+=task[1]
        return result
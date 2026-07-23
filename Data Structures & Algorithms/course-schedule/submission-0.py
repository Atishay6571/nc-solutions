class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs=defaultdict(list) # Course C1 has: These Prereqs
        requirement=defaultdict(list) #Course C1 is a requirement in: C2
        for a,b in prerequisites:
            prereqs[a].append(b)
            requirement[b].append(a)
        
        #now check for any course available that does not have prereqs
        def bfs():
            queue=deque()
            #must track how many courses were processed
            processed=0
            for course in range(numCourses):
                if course not in prereqs: 
                    queue.append(course) #set on the path of removal/clearance
            
            while queue:
                course=queue.popleft()
                processed+=1
                for requires in requirement[course]:
                    prereqs[requires].remove(course)
                    if len(prereqs[requires])==0:
                        queue.append(requires)
            if processed==numCourses:
                return True
            return False
        return bfs()
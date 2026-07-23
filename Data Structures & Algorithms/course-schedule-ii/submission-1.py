class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Kahn's Algorithm
        #Uses BFS
        requires={i:[] for i in range(numCourses)}
        prereqs=defaultdict(list)
        for a,b in prerequisites:
            prereqs[a].append(b)
            requires[b].append(a)
        queue=deque()
        for course in range(numCourses):
            if prereqs[course]==[]:
                queue.append(course)
        result=[]
        while queue:
            course=queue.popleft()
            result.append(course)
            for req in requires[course]:
                prereqs[req].remove(course)
                if len(prereqs[req])==0:
                    queue.append(req)
        if len(result)!=numCourses:
            return []
        return result

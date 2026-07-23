class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        prereqs = defaultdict(list)
        for a, b in prerequisites:
            prereqs[b].append(a)

        reachable = defaultdict(set)
        visited = set()

        def dfs(node):
            if node in visited:
                return reachable[node]
            visited.add(node)
            for neighbor in prereqs[node]:
                reachable[node].add(neighbor)
                reachable[node] |= dfs(neighbor)
            return reachable[node]

        for i in range(numCourses):
            dfs(i)

        return [a in reachable[b] for a, b in queries]
        



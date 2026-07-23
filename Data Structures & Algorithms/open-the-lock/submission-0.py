class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def neighbors(state):
            result = []
            for i in range(4):
                digit = int(state[i])
                up = state[:i] + str((digit + 1) % 10) + state[i+1:]
                down = state[:i] + str((digit - 1) % 10) + state[i+1:]
                result.append(up)
                result.append(down)
            return result

        def bfs():
            queue=deque()
            queue.append("0000")
            rotations=0
            while queue:
                for i in range(len(queue)):
                    state=queue.popleft()
                    for neighbor in neighbors(state):
                        if neighbor not in deadends and neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
                    if state==target:
                        return rotations
                    
                rotations+=1
            return -1
        if "0000" in deadends:
            return -1
        visited=set()
        visited.add("0000")
        return bfs()
                
        
            
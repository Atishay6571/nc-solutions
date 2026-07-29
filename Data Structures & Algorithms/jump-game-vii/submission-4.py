class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue=deque()
        queue.append(0)
        farthest=0  #largest visited, to prevent repetitive work
        while queue:
            index = queue.popleft()
            if index==(len(s)-1):
                return True
            for i in range(max(farthest+1, index+minJump), index+maxJump+1):
                if i<len(s) and s[i]=="0":
                    queue.append(i)
            farthest=max(farthest,index+maxJump)
            
        return False

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        for i in range(len(speed)):
            stack.append([position[i],speed[i]])
        stack.sort(reverse=True)
        fleets=1
        for i in range (len(stack)-1):
            if (target-stack[i][0])/stack[i][1]< (target-stack[i+1][0])/stack[i+1][1]:
                fleets+=1
            else:
                stack[i+1]=stack[i]
        return fleets     
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)
        stack=[] #pair of (temps , indexes)
        for i in range(len(temperatures)):

            while stack:
                a=stack.pop()
                if temperatures[i]>a[0]:
                    answer[a[1]]=i-a[1]
                else:
                    stack.append(a)
                    stack.append([temperatures[i],i])
                    break
            stack.append([temperatures[i],i])
        return answer


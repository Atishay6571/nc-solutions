class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        result=[]
        for i in asteroids:
            if i>0:
                stack.append(i)
            else:
                while stack:
                    a=stack.pop()
                    if abs(a)>abs(i):
                        stack.append(a)
                        break
                    elif abs(a)==abs(i):
                        break
                else:
                    result.append(i)
        while stack:
            result.append(stack.pop(0))
        return result

            
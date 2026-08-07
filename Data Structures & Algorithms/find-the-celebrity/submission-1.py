# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        indeg = [0]*n
        outdeg = [0]*n
        for i in range(n):
            for j in range(n):
                if knows(i,j):
                    indeg[j]+=1
                    outdeg[i]+=1
        if (n) in indeg:
            index=  indeg.index(n)
            if outdeg[index]==1:
                return index
        return -1
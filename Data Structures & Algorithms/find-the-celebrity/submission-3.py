# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        for i in range(n):
            if i== candidate:
                continue
            if not knows(i, candidate) or knows(candidate, i):
                return -1
        return candidate


#If knows(candidate, i) is true, the candidate knows someone and is out. If false, i isn't known by everyone and they're out. Either way you advance having eliminated one person, so after n-1 calls exactly one survivor remains.
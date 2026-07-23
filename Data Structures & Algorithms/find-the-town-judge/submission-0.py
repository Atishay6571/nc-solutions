class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #construct graph first
        #since the town judge trusts noone, easy to check
        #now need trust graphs to show that everyone trusts townjudge
        from collections import defaultdict
        trustees=defaultdict(list)
        trustsSomeone=set()
        possibleAnswer=[]
        for a,b in trust:
            trustees[b].append(a)
            trustsSomeone.add(a)
            if len(trustees[b])==(n-1):
                possibleAnswer.append(b)
        for ans in possibleAnswer:
            if ans not in trustsSomeone:
                return ans
        else:
            return -1
                  

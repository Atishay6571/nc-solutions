class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #if cost[i] >= gas[i], ith station cant be starting
        if sum(gas)<sum(cost):
            return -1
        n=len(gas)
        tank=0
        start=0
        for i in range(n):
            tank+=(gas[i]-cost[i])
            if tank<0:
                tank=0
                start=i+1
        return start

    '''Key idea 1: If sum(gas) < sum(cost), no solution exists.

    Key idea 2: If your tank goes negative at station i, then 
    every station between your start and i is also a bad start. 
    Why? They all have even less fuel accumulated when they reach i.
    So skip all of them — start from i + 1.'''
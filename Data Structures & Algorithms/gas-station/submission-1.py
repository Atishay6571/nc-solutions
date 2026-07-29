class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #if cost[i] >= gas[i], ith station cant be starting
        n=len(gas)
        for i in range(n): #considering each as starting station
            fuel=0
            if cost[i]>gas[i]:
                continue
            for j in range(i,i+n):
                station= j%n
                fuel+=gas[station]
                if fuel>=cost[station]:
                    fuel-=cost[station]
                    continue
                else:
                    break
            else:
                return i
        return -1
        
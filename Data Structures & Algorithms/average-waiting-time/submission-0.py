class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_wait = 0
        curr = 0
        for arrive, time in customers:
            total_wait += time
            if arrive >= curr: # no wait at all
                curr = time + arrive
                continue
            else:
                total_wait += (curr - arrive)
                curr += time
        return total_wait/len(customers)
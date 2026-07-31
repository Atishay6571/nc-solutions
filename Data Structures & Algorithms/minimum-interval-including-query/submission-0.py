class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # queries.sort() cant sort directly as 
        intervals.sort()
        mheap=[] # (length, end)
        hashmap={} # to store answers for queries
        i = 0  # pointer into intervals, never goes backwards

        for q in sorted(queries):
            # push all intervals starting <= q
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i][0], intervals[i][1]
                heapq.heappush(mheap, (end - start + 1 , end))
                i += 1    # never resets, just moves forward
            
            # pop expired intervals
            while mheap and q > mheap[0][1]:
                heapq.heappop(mheap)
            # answer = top of heap
            hashmap[q]= mheap[0][0] if mheap else -1

        result=[]
        for q in queries:
            result.append(hashmap[q])
        return result



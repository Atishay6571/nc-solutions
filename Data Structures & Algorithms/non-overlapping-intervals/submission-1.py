class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end time, if overlap with prev, keep the previous one 
        intervals.sort(key = lambda x : x[1])
        prev_end = intervals[0][1]
        removal_count=0
        for i in range(1, len(intervals)):
            if intervals[i][0]>= prev_end:
                prev_end = intervals[i][1]
                continue
            else:  
                removal_count+=1
        return removal_count
                

        
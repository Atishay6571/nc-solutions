class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]
        for index, (start,end) in enumerate(intervals):
            if end < newInterval[0]:  # the current interval finished before new starts
                result.append((start,end))
            elif start> newInterval[1]:  # the new interval finished before current one starts
                result.append(newInterval)
                result.extend(intervals[index::])
                return result
            else: #either new end doesnt end before current start OR new start doesnt start soon   
                newInterval=((min(start,newInterval[0]), max(end, newInterval[1])))
        result.append(newInterval)
        return result

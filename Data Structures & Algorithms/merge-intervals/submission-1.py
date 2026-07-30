class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result=[]
        intervals.sort()
        for start,end in intervals:
            if not result:
                result.append((start,end))
            if start > result[-1][1]:
                result.append((start,end))
            result[-1]=( min(result[-1][0], start), max( result[-1][1], end) )
        return result

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        for interval in range( 1, len(intervals)):
            if intervals[interval].start>= intervals[interval-1].end:
                continue
            return False
        return True
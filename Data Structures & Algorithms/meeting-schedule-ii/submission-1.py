"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort ( key= lambda x: x.start)   #sort by end times
        rooms=[] # stores the end of the last meeting
        if not intervals:
            return 0
        rooms.append(intervals[0].end)
        for i in range(1, len(intervals)):
            if intervals[i].start< intervals[i-1].end: # overlap conflict
                for index,end in enumerate(rooms):
                    if intervals[i].start>= end:
                        rooms[index]=intervals[i].end
                        break
                else:
                    rooms.append(intervals[i].end)
        return len(rooms)
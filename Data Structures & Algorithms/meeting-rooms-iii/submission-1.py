class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # must track number of meetings per room
        # must also track earliest meeting end time 
        # must track initial occupied or not with an array
        meetings.sort()

        mheap = []  # occupied rooms: (end_time, room)

        # CHANGED: Maintain a separate min-heap of available room numbers
        available = [i for i in range(n)]
        heapq.heapify(available)

        count = [0 for _ in range(n)]

        for meeting in meetings:

            # CHANGED: Free ALL rooms that have finished before this meeting starts
            while mheap and mheap[0][0] <= meeting[0]:
                prev_end, room = heapq.heappop(mheap)
                heapq.heappush(available, room)

            # CHANGED: If any room is available, always use the smallest room number
            if available:
                room = heapq.heappop(available)
                heapq.heappush(mheap, (meeting[1], room))
                count[room] += 1

            else:
                # No room free -> delay meeting
                prev_end, room = heapq.heappop(mheap)
                heapq.heappush(
                    mheap,
                    (meeting[1] + (prev_end - meeting[0]), room)
                )
                count[room] += 1

        maximum = max(count)
        for i, val in enumerate(count):
            if val == maximum:
                return i
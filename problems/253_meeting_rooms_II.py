'''
# TAG-HEAP, TAG-GRDY
# N.B.: 

sort by start time, and track earliest ending times
we can re-use a room by (greedily) assigning the next earliest starting to the latest ending
'''

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x[0])

        min_heap = []
        heapq.heappush(min_heap, intervals[0][1])
        
        for it in range(len(intervals)):
            start, end = intervals[it]

            # if the next meeting's starting time is after the earliest ending time,
            # we can re-use a room
            if start >= min_heap[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, end)
        
        # heaps have dynamic sizing!
        return len(min_heap)

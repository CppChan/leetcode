# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1



# 先排序，
# 最小堆，存放每个房间的结束时间

import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
    	if len(intervals)==0:return 0
    	intervals.sort(key = lambda x: x.start)
    	room = [intervals[0].end]
    	heapq.heapify(room)
    	for i in range(1, len(intervals)):
    		if intervals[i].start>=room[0]:heapq.heappop(room)
    		heapq.heappush(room, intervals[i].end)
    	return len(room)
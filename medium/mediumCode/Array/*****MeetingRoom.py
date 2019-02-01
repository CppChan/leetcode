# method 1

#use +1 and -1 to indicate start and end time in a time lists
#think like +1 means open a room for use(may be new or has previously used), -1 means temporary close a room(but may be for future use)
# and num means the number of room now being used, res means how many rooms has opened

class Solution(object):
  def minMeetingRooms(self, interval):
  	if len(interval)==0 or len(interval)==1:return 1
  	mint,maxt = 0,0
  	for i in range(len(interval)):
  		mint = min(mint, interval[i][0])
  		maxt = max(maxt, interval[i][1])
  	time = [0]*(maxt-mint+1)
  	for i in range(len(interval)):
  		time[interval[i][0]]+=1
  		time[interval[i][1]]-=1
  	num,res=0,0
  	for i in range(len(time)):
  		num+=time[i]
  		res = max(res, num) #when room be open, it will be count into res
  	return res

# method 2
import heapq

def minMeetingRooms(self, intervals):
	if len(intervals) == 0: return 0
	intervals.sort(key=lambda x: x.start)
	room = [intervals[0].end]
	heapq.heapify(room)
	for i in range(1, len(intervals)):
		if intervals[i].start >= room[0]: heapq.heappop(room)
		heapq.heappush(room, intervals[i].end)
	return len(room)





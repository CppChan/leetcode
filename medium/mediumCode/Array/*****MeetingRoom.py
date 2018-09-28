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
  		res = max(res, num)
  	return res

#use +1 and -1 to indicate start and end time in a time lists

#or can use sort and greedy and heap

# public class Solution {
#     public int minMeetingRooms(Interval[] intervals) {
#         if(intervals == null || intervals.length == 0) return 0;
#         Arrays.sort(intervals, new Comparator<Interval>(){
#            @Override
#            public int compare(Interval a, Interval b){
#                return (a.start - b.start);
#            }
#         });
#
#         PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
#         pq.add(intervals[0].end);
#         for(int i=1; i<intervals.length; i++){
#             if(intervals[i].start >= pq.peek()){
#                 pq.poll();
#             }
#             pq.add(intervals[i].end);
#         }
#         return pq.size();
#     }
# }


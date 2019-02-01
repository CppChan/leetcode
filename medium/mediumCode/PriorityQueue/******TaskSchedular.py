# O(n) time an O(1) space solution

# https://leetcode.com/problems/task-scheduler/discuss/104496/concise-Java-Solution-O(N)-time-O(26)-space

# public class Solution {
#     public int leastInterval(char[] tasks, int n) {
#
#         int[] c = new int[26];
#         for(char t : tasks){
#             c[t - 'A']++;
#         }
#         Arrays.sort(c);
#         int i = 25;
#         while(i >= 0 && c[i] == c[25]) i--; // get most frequency task set
#
#         return Math.max(tasks.length, (c[25] - 1) * (n + 1) + 25 - i);
#     }
# }



# Examples:
#
# AAAABBBEEFFGG 3
#
# here X represents a space gap:
#
# Frame: "AXXXAXXXAXXXA"
# insert 'B': "ABXXABXXABXXA" <--- 'B' has higher frequency than the other characters, insert it first.
# insert 'E': "ABEXABEXABXXA"
# insert 'F': "ABEFABEXABFXA" <--- each time try to fill the k-1 gaps as full or evenly as possible.
# insert 'G': "ABEFABEGABFGA"
# AACCCBEEE 2
#
# 3 identical chunks "CE", "CE CE CE" <-- this is a frame
# insert 'A' among the gaps of chunks since it has higher frequency than 'B' ---> "CEACEACE"
# insert 'B' ---> "CEABCEACE" <----- result is tasks.length;
# AACCCDDEEE 3
#
# 3 identical chunks "CE", "CE CE CE" <--- this is a frame.
# Begin to insert 'A'->"CEA CEA CE"
# Begin to insert 'B'->"CEABCEABCE" <---- result is tasks.length;
# ACCCEEE 2
#
# 3 identical chunks "CE", "CE CE CE" <-- this is a frame
# Begin to insert 'A' --> "CEACE CE" <-- result is (c[25] - 1) * (n + 1) + 25 -i = 2 * 3 + 2 = 8



import heapq
from collections import defaultdict
class Solution(object):
	def leastInterval(self, tasks, n):
		tasklist, taskdict,n= [], defaultdict(lambda: 0),n+1
		for i in range(len(tasks)):
			taskdict[tasks[i]] += 1
		for item in taskdict.items():
			tasklist.append(-item[1])
		heapq.heapify(tasklist)
		res, n_ = 0, n
		while len(tasklist) > 0:
			templist, n = [], n_
			while n > 0 and len(tasklist) > 0:
				temp = -heapq.heappop(tasklist)
				temp -= 1
				if temp> 0: templist.append(-temp)
				n -= 1
			if len(templist) == 0 and len(tasklist) == 0:
				res += (n_ - n)
				break
			while len(templist) > 0:
				heapq.heappush(tasklist, templist[-1])
				templist.pop()
			res += n_
		return res

if __name__=="__main__":
	s = Solution()
	s.leastInterval(["A","B","C","A","B"],2)
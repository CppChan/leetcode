import heapq
class linklist(object):
	def __init__(self, ListNode):
		self.node = ListNode
	def __cmp__(self, other):
		return self.node.val-other.node.val
class Solution(object):
    def mergeKLists(self, lists):
        list = []# here use a new array is to avoid lists[i]==None
    	for i in range(len(lists)):
    		if lists[i]: list.append(linklist(lists[i]))
    	heapq.heapify(list)
    	res = ListNode(0)
        cur = res
    	while len(list)>0:
    		temp = heapq.heappop(list)
    		cur.next = ListNode(temp.node.val)
    		cur = cur.next
    		temp.node = temp.node.next
    		if temp.node: heapq.heappush(list,temp)
    	return res.next
class Solution(object):
  def deleteNodes(self, head, indices):
  	dummy = ListNode(0)
  	dummy.next = head
  	cur = dummy
  	i= 0
  	while cur.next and len(indices)>0:
  		if i == indices[0]:
  			cur.next = cur.next.next
  			indices.pop(0)
  			i+=1
  			continue
  		i+=1
  		cur=cur.next
  	return dummy.next
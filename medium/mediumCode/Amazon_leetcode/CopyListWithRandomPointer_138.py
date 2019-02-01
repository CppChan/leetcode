
class Solution(object):
  def copyRandomList(self, head):
  	if not head:return None
  	res = RandomListNode(head.label)
  	dic = {head.label:res}
  	while head:
  		temp = dic[head.label]
  		if head.next and head.next.label not in dic: dic[head.next.label] = RandomListNode(head.next.label)
  		if head.next: temp.next = dic[head.next.label]
  		if head.random and head.random.label not in dic: dic[head.random.label] = RandomListNode(head.random.label)
  		if head.random: temp.random = dic[head.random.label]
  		head = head.next
  	return res
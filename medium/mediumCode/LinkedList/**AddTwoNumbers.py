# You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#https://leetcode.com/problems/add-two-numbers-ii/
class Solution(object):
	def addTwoNumbers(self, l1, l2):
		if not l1: return l2
		elif not l2: return l1
		size1, size2 = self.computelength(l1), self.computelength(l2)
		if size2<size1: l1,l2 = l2,l1
		res = self.addTwoNumbers1(l1, l2, abs(size1-size2))
		if res[1]>0: #dont forget this cornercase, when finally add >0 , one more listnode
			head = ListNode(res[1])
			head.next = res[0]
			return head
		return res[0]
	def addTwoNumbers1(self, l1, l2, dif):#dif is the length difference between to sequence
		if not l1.next and not l2.next: return (ListNode((l1.val+l2.val)%10), (l1.val+l2.val)/10)
		back = None
		if dif>0: back = self.addTwoNumbers1(l1, l2.next, dif-1) # not duiqi
		else: back = self.addTwoNumbers1(l1.next, l2.next, dif)
		val, add = 0,0
		if dif == 0: val, add = (l1.val+l2.val+back[1])%10, (l1.val+l2.val+back[1])/10
		else: val, add = (l2.val+back[1])%10, (l2.val+back[1])/10# only add one number
		curnode = ListNode(val)
		curnode.next = back[0]
		return(curnode, add)
	def computelength(self, Node):
		length = 0
		while Node:
			length+=1
 			Node = Node.next
		return length
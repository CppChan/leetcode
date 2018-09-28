class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def selectionSort(self, head):
		dummy = ListNode(0)
		dummy.next = head
		list = dummy
		size= 0
		while list.next:
			size+= 1
			list = list.next
		if size == 0 or size == 1:
			return dummy.next
		list = dummy
		maxNodepre = ListNode(0)
		maxNodepre.next = ListNode(0)
		while size>1:
			i = 0
			maxNodepreIndex = 0
			while i<size:
				if list.next.val>maxNodepre.next.val:
					maxNodepre = list
					maxNodepreIndex = i
				if i != size-1:
					list = list.next
				i+=1
			i-=1
			if maxNodepreIndex == i:
				maxNodepreIndex = 0
			elif maxNodepreIndex == i-1:
				tempLastPlus = list.next.next
				maxNodepre.next = list.next
				maxNodepre.next.next = list
				list.next = tempLastPlus
			elif maxNodepreIndex == i-2:
				tempMaxNext= maxNodepre.next
				tempLastPlus = list.next.next
				maxNodepre.next = list.next
				maxNodepre.next.next = list
				list.next = tempMaxNext
				list.next.next = tempLastPlus
			else:
				tempLast = list.next
				tempMaxNext= maxNodepre.next
				tempMaxNextNext = maxNodepre.next.next
				tempLastPlus = tempLast.next
				tempLast.next = tempMaxNextNext
				maxNodepre.next = tempLast
				tempMaxNext.next = tempLastPlus
				list.next = tempMaxNext
			size-=1
			list = dummy
			maxNodepre = ListNode(0)
			maxNodepre.next = ListNode(0)
		return dummy.next

if __name__ == "__main__":
    s = Solution()
    [5, 4, 1, 2, 6, 3]
    one = ListNode(4)
    one.next = ListNode(3)
    one.next.next = ListNode(2)
    one.next.next.next = ListNode(1)
    # one.next.next.next.next = ListNode(6)
    # one.next.next.next.next.next = ListNode(3)
    s.selectionSort(one)

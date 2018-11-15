class Solution(object):
	def findmid(self, input):
		i,j,change=0,len(input)-1,0
		while i<j-1:
			mid = (i+j)/2
			if input[mid]>input[mid-1] and input[mid]>input[mid]+1:
				change = mid
				break
			if input[mid]>input[0] and input[mid]>input[-1]: i = mid
			elif input[mid]<input[-1] and input[mid]<input[0]: j = mid
		if i==0 and input[i]>input[i+1] or (input[i]>input[i-1] and input[i]>input[i+1]):change = i
		else: change = j
		mid = len(input)/2
		if len(input)%2==1:
			if mid<=change:return input[change-mid]
			else: return input[len(input)-(mid-change)]
		else:
			mid -=1
			if change == mid: return float((input[0]+input[-1]))/2
			elif change<mid: return float((input[len(input)-(mid-change)]+input[len(input)-(mid-change)-1]))/2
			else: return float((input[change-mid]+input[change-mid-1]))/2


if __name__ == "__main__":
    s=Solution()
    print s.findmid([5,6,7,8,9,1,3])
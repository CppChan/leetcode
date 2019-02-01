class Solution(object):
	def add(self, input):
		num, left= 0, 0
		for i in range(len(input)):
			if input[i]==")" and num == 0: left+=1
			else:
				if input[i]==")": num-=1
				else: num+=1
		right = num
		return (left, right)


s = Solution()
print s.add(')(()(')
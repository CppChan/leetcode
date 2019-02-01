class Solution(object):
  	def reverseWords(self, input):
		input = list(input)#this is important
		self.reverse(input, 0, len(input)-1)
		i ,left, right= 0, 0, 0
		while i<len(input):
			if i==len(input)-1 or input[i+1]==" ":
				right = i
				self.reverse(input, left, right)
				left = i+2
			i+=1
		return "".join(input)

  	def reverse(self, input,left,right):
		while left<right:
			input[left], input[right]=input[right], input[left]
			left+=1
			right-=1


s = Solution()
print s.reverseWords("Hello, I'm Xijia")
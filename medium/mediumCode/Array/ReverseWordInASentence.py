# class Solution(object):
#   def reverseWords(self, input):
#   	list = input.split(" ")
#   	i = 0
#   	while i < len(list):
#   		if list[i]=="" or list[i]==" ": list.pop(i)
#   		else:
#   			if list[i][0]==" ": list[i]=list[i][1:len(list[i])]
#   			i+=1
#   	list.reverse()
#   	return " ".join(list)
#
class Solution(object):# not strip split join version
  def reverseWords(self, input):
  	input = list(input)
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


if __name__=="__main__":
    s = Solution()
    # s.reverseWords(" A B C D ")
    list = " A B C D ".split(" ")
    print list
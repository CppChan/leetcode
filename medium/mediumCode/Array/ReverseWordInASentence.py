class Solution(object):
  def reverseWords(self, input):
  	list = input.split(" ")
  	i = 0
  	while i < len(list):
  		if list[i]=="" or list[i]==" ": list.pop(i)
  		else:
  			if list[i][0]==" ": list[i]=list[i][1:len(list[i])]
  			i+=1
  	list.reverse()
  	return " ".join(list)


if __name__=="__main__":
    s = Solution()
    # s.reverseWords(" A B C D ")
    list = " A B C D ".split(" ")
    print list
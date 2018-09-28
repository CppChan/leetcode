class Solution(object):
  def decompress(self, input):
  	if len(input)==0:return input
  	i,input= 0,list(input)
  	while i < len(input):
  		if not input[i].isdigit():i+=1
  		else:
  			long = int(input[i])-1
  			if long<0:
  				input.pop(i-1)
  				input.pop(i-1)
  				continue
  			temp = input[i-1]*(long)
  			input.pop(i)
  			input.insert(i, temp)
  			i+=1#!!!!! here append"ccc" not "c", "c", "c"
  	return "".join(input)

if __name__ == "__main__":
    s = Solution()
    print s.decompress("a0b1c4d1")
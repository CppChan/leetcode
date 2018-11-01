class Solution(object):
  def reverse(self, source):
  	i, source = 0, list(source)
  	source.reverse()
  	source = "".join(source)
  	while i < len(source):
  		if not source[i].isdigit() and source[j+1]!=".":
  			i+=1
  			continue
  		j = i
  		while j<len(source):
  			if source[j].isdigit() or source[j]==".":j+=1
  			else:break
  		newstring = list(source[i:j])
  		newstring.reverse()
  		newstring = "".join(newstring)
  		if j<len(source) and source[j]=="-" and not source[j+1].isdigit() and source[j+1]!=".":
  			newstring = "-"+newstring
  			j+=1
  		source = source[:i]+newstring+source[j:len(source)]
  		i = j
  	return source

if __name__ == "__main__":
    s = Solution()
    print s.reverse("1*2.4+-9.3-2.44/5.34")
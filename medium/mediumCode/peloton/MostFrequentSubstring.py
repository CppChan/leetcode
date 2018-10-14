from collections import defaultdict
class Solution(object):
  def mostFrequentSubstring(self, input,min,max,unique):
  	substring_count,input,res = defaultdict(lambda:0),list(input),0
  	for i in range(len(input)-min+1):
  		substring= input[i:i+min]
  		substring_set = set(substring)
  		while len(substring)<=max and len(substring_set)<=unique:
  			substring_count["".join(substring)]+=1
  			if substring_count["".join(substring)]>res:res = substring_count["".join(substring)]
  			if i+len(substring)<len(input):
  				newletter = input[i+len(substring)]
  				substring.append(newletter)
  				substring_set.add(newletter)
  			else:break
  	return res


if __name__ == "__main__":
    s =Solution()
    print s.mostFrequentSubstring("abcddabcefcdaaafcdda", 2, 5, 3)
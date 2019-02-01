#maintain two pointers


class Solution(object):
  def lengthOfLongestSubstring(self, s):
    dic,length,res= {},0,[]
    i,j = 0,0
    while j<len(s):
    	if s[j] in dic and dic[s[j]]>=i:i = dic[s[j]]+1#corner!!!!! second condition
    	dic[s[j]]=j
    	if j-i+1>length:
    		res = [s[i:j+1]]
    		length = j-i+1
    	elif j-i+1 == length: res.append(s[i:j+1])
    	j+=1
    return length


s = Solution()
print s.lengthOfLongestSubstring("abba")
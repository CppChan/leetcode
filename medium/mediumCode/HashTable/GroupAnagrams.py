class Solution(object):
  def groupAnagrams(self, strs):
  	dic, res= {},[]
  	for item in strs:
  		hashkey = self.convert(item)
  		if hashkey in dic: dic[hashkey].append(item)
  		else: dic[hashkey] = [item]
  	for t in dic.iteritems():
  		res.append(t[1])
  	return res

  def convert(self, s):
  	res = [0]*26
  	for char in s:
  		res[ord(char)-ord('a')] += 1
  	return tuple(res)
class Solution(object):
  def find(self, input, k):
  	dic, repeat,res= {}, set([]),[]
  	if k>len(input):return []
  	if k==len(input):
  		res = set(input)
  		if len(res)<len(input):return []
  		else:return input
  	for i in range(k):
  		if input[i] not in dic:dic[input[i]]=1
  		else:
  			dic[input[i]]+=1
  			set.add(input[i])
  	for i in range(k,len(input)):
  		if len(repeat)==0: res.append(input[i-k:i])
  		dic[input[i-k]]-=1
  		if dic[input[i-k]]==1:repeat.remove(input[i-k])
  		if input[i] in dic:dic[input[i]]+=1
  		else:dic[input[i]]=1
  		if dic[input[i]]>1:repeat.add(input[i])
  	if len(repeat)==0:res.append(input[len(input)-k:len(input)])
  	return res

  def findStringLengthK(input, k): #exactly len(substring)=k
    if k == 0 or not input: return []
    exist = {}
    ret = []
    lo = 0
    for i in range(len(input)):
        if input[i] in exist:
            idx = exist[input[i]]
            for j in range(lo, idx): exist.pop(input[j])
            lo = idx+1
        else:
            if i - lo + 1 > k:
                exist.pop(input[lo])
                lo += 1
        exist[input[i]] = i
        if i-lo+1 == k: ret.append(input[lo:i+1])
    return ret

  def findStringLengthK2(self, input, k):#len(substring) can > k
  	if len(input)==0 or k == 0:return []
  	if k==1:return input.split("")
  	res, dic= [],[0]*26
  	for i in range(len(input)):
  		dic, dist= [0]*26, 0
  		for j in range(i, len(input)):
  			if dic[ord(input[j])-ord('a')] == 0: dist+=1
  			dic[ord(input[j])-ord('a')]+=1
  			if dist == k: res.append(input[i:j+1])
  			elif dist>k: break
  	return res

if __name__ == "__main__":
    s = Solution()
    print s.find("barfoothefoobarman",4)
    print s.findStringLengthK2("barfoothefoobarman",4)
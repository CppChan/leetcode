class Solution(object):
  def allAnagrams1(self, p,s):
        res = []
        n, m = len(s), len(p)
        if n < m: return res
        phash, shash = [0]*123, [0]*123
        for x in p:
            phash[ord(x)] += 1
        for x in s[:m-1]:
            shash[ord(x)] += 1 # use ord to indicate ascii
        for i in range(m-1, n):
            shash[ord(s[i])] += 1
            if i-m >= 0:
                shash[ord(s[i-m])] -= 1
            if shash == phash:
                res.append(i - m + 1)
        return res

  def allAnagrams2(self, p,s):# better solution with two pointers(windows) similar with smallest substring containing another string
  	dic,res = {},[]
  	for i in range(len(p)):
  		if not dic.has_key(p[i]):dic[p[i]]=1
  		else: dic[p[i]]+=1
  	i,j,counter=0,0,len(dic)
  	while i <len(s) and j<len(s):
  		if dic.has_key(s[j]):
  			dic[s[j]]-=1# val in key-value pair can be negative, indicating that count a certain element more than string p need.
  			if dic[s[j]]==0: counter-=1# when a element in p is count enough, counter-=1
  		j+=1
  		while counter==0:# counter==0 means all the element in p is find enough
  			if dic.has_key(s[i]):
  				dic[s[i]]+=1
  				if dic[s[i]]>0: counter+=1# we need this certain element again
  			if counter>0 and j-i==len(p): res.append(i)#check the length
  			i+=1
  	return res

#https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.
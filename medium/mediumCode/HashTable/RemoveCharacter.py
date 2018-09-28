class Solution(object):
  def remove(self, large, small):
  	if len(small)==0:return 0
  	if len(small)==1:
  		j = 0
  		while j<len(large):
  			if large[j]==small:
  				large = large[:j]+large[j+1:len(large)]
  				continue
  			j+=1
  		return large
  	dic = {}
  	for i in range(len(small)):#make a letter:index dictionary
  		if not dic.has_key(small[i]):dic[small[i]]=[i]
  		else:dic[small[i]].append(i)
  	indexdic, newdic= set([]),set([])
  	while i<len(large):
  		if large[i]==small[-1] and (len(small)-1) in indexdic:
  			large = large[:i-len(small)+1]+large[i+1:len(large)]
  			i-=len(small)-1
  			indexdic=set([])
  			continue
  		if not dic.has_key(large[i]):#not contains this letter, clear up indexdic
  			indexdic = set([])
  			i+=1
  			continue
  		index = dic[large[i]]
  		if large[i]==small[0]:#if it is small[0]
  			newdic.add(1)
  		for j in index:
  			if j in indexdic:#update the index of the next expected letter in small
  				newdic.add(j+1)
  		indexdic = newdic
  		newdic = set([])
  		i+=1
  	return large


if __name__=="__main__":
    s=Solution()
    print s.remove("aaabcabca","bc")
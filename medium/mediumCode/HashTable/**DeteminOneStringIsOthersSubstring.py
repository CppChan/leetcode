class Solution(object):
  def strstr(self, large, small):
  	if len(small)==0:return 0
  	if len(small)==1:
  		for j in range(len(large)):
  			if large[j]==small[0]:return j
  	dic = {}
  	for i in range(len(small)):#make a letter:index dictionary
  		if not dic.has_key(small[i]):dic[small[i]]=[i]
  		else:dic[small[i]].append(i)
  	indexdic, newdic= set([]),set([])
  	for i in range(len(large)):
  		if large[i]==small[-1] and (len(small)-1) in indexdic: return i - len(small)+1#return result
  		if not dic.has_key(large[i]):#not contains this letter, clear up indexdic
  			indexdic = set([])
  			continue
  		index = dic[large[i]]
  		if large[i]==small[0]:#if it is small[0]
  			newdic.add(1)
  		for j in index:
  			if j in indexdic:#update the index of the next expected letter in small
  				newdic.add(j+1)
  		indexdic = newdic
  		newdic = set([])
  	return -1


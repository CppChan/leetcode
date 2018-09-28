class Solution(object):
  def wordsToExclude(self,text, exclude):
  	ex_list = set([])
  	for word in exclude:
  		ex_list.add(word.lower())#lower!!!
  	max_count, dic, i, res=0, {},0,[]
  	while i<len(text):
  		if text[i].isalpha():
  			index = i
  			while text[i].isalpha():i+=1#isalpha()
  			word = text[index:i].lower()
  			if word in ex_list:continue
  			if word not in dic: dic[word]=1
  			else: dic[word]+=1
  			max_count = max(max_count, dic[word])
  		else: i+=1
  	for item in dic.iteritems():
  		if item[1]==max_count:
  		    res.append(item[0])
  	return res

if __name__ == "__main__":
    s = Solution()
    text = "Jack and Jill went to the market to buy bread and cheese. Cheese is Jack's and Jill's favorite food."
    exclude = ['and', 'he', 'the', 'to', 'is', 'Jack', 'Jill']
    print(s.wordsToExclude(text, exclude))
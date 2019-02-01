class Solution(object):

	#bidirectional bfs , time complexity is  sqrt(O(bfs)), which is 2* O(b^(d/2)), where b is the number of children in tree, d is the depth.
    def ladderLength(self, beginWord, endWord, wordList):
        wordList, beginset, endset= set(wordList),set([beginWord]), set([endWord])
        if endWord not in wordList: return 0
        step = self.search(beginset, endset, wordList,0)
        if step==0:return 0
        else: return step+1

    def search(self, beginset, endset, wordList, step):
    	if len(beginset)==0 or len(endset)==0: return 0
    	wordList-=beginset
    	beginlist, nextlevel= list(beginset), []
    	for i in range(len(beginlist)):
    		word = beginlist[i]
    		for k in range(len(word)):
    			for j in range(ord("a"),ord("z")+1):
    				temp= word[:k]+chr(j)+word[k+1:]
    				if temp not in wordList:continue
    				if temp in endset: return step+1
    				nextlevel.append(temp)
    	if len(nextlevel)>len(endset): return self.search(endset, set(nextlevel), wordList,step+1)# let the shorter list to generate next level
    	else: return self.search(set(nextlevel), endset, wordList,step+1)


    def ladderLength2(self, beginWord, endWord, wordList):
        wordList = set(wordList)
    	level, res = [beginWord], 0
    	while len(level)>0:
    		nextlevel = self.findnextlevel(level, endWord, wordList)
    		res+=1
    		if nextlevel=="find": return res+1
    		level = nextlevel
    	return 0

    def findnextlevel(self, level, endWord, wordList):
    	nextlevel = []
    	for i in range(len(level)):
    		word = level[i]
    		for k in range(len(word)):
    			for j in range(ord("a"),ord("z")+1):
    				pre = word[k]
    				word = word[:k]+chr(j)+word[k+1:]
    				if word in wordList:
    					nextlevel.append(word)
    					wordList.remove(word)
    					if word == endWord: return "find"
    				word = word[:k]+pre+word[k+1:]
    	return nextlevel

		def ladderLength(self, beginWord, endWord, wordList):
			left, right, leftqueue, rightqueue = 0, 0, [beginWord], [endWord]
			wordList = set(wordList)
			if endWord not in wordList: return 0
			wordList.remove(endWord)
			while len(wordList) > 0:
				left += 1
				newleftqueue = []
				if self.operation(leftqueue, newleftqueue, set(rightqueue), wordList): return left + right + 1
				if len(newleftqueue) == 0: break
				right += 1
				newrightqueue = []
				if self.operation(rightqueue, newrightqueue, set(newleftqueue), wordList): return left + right + 1
				if len(newrightqueue) == 0: break
				leftqueue = newleftqueue
				rightqueue = newrightqueue
			return 0

		def operation(self, queue, newqueue, otherqueue, wordList):
			for i in range(len(queue)):
				word = queue[i]
				for j in range(len(word)):
					for k in range(ord("a"), ord("z") + 1):
						if word[j] == chr(k): continue
						newword = word[:j] + chr(k) + word[j + 1:]
						if newword in otherqueue: return True
						if newword in wordList:
							wordList.remove(newword)
							newqueue.append(newword)
			return False

if __name__=="__main__":
    s = Solution()
    print s.ladderLength3("hit","cog",["hot","cog"])
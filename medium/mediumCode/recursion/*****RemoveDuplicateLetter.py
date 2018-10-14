class Solution(object):
  def removeDuplicateLetters(self, s):
  	if len(s)==0:return ""
  	s = list(s)
  	letter = [0]*26
  	for i in range(len(s)):
  		letter[ord(s[i])-ord('a')]+=1#count nunm
  	best=0
  	for i in range(len(s)):
  		if ord(s[i])-ord('a')<ord(s[best])-ord('a'):best=i
  		letter[ord(s[i])-ord('a')]-=1
  		if letter[ord(s[i])-ord('a')]==0:break#if a letter is ran out of, then break, because after that letter, can not form a right res.
  	back = s[best+1:len(s)]
  	i = 0
  	while i<len(back):
  		if back[i]==s[best]:back.pop(i)
  		else:i+=1
  	return s[best]+self.removeDuplicateLetters(back)


#generally, each time, add a smallest letter to res and maintain that the substring after that letter contains at least one of every letter in original s.

#https://leetcode.com/problems/remove-duplicate-letters/discuss/76768/A-short-O(n)-recursive-greedy-solution
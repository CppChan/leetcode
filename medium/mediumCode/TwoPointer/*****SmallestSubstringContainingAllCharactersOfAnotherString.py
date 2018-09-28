class Solution(object):
  def smallest(self, s1, s2):
  	if not s2:return 0
  	dic,missing = {},len(s2)
  	for i in range(len(s2)):
  		if not dic.has_key(s2[i]): dic[s2[i]]=1
  		else: dic[s2[i]]+=1
  	i=I=J=0
 	for j in range(len(s1)):
 		if s1[j] in dic:
 			if dic[s1[j]]>0:missing-=1
 			dic[s1[j]]-=1
 		if not missing:
 			while i<j and (not dic.has_key(s1[i]) or dic[s1[i]]<0):
 				if dic.has_key(s1[i]):dic[s1[i]]+=1
 				i+=1
 			if not J or j-i<J-I: J,I = j,i
 	if missing>0:return ""
 	return s1[I:J+1]

#https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python

# Use dic to record how many certain letter still need to add to the window ,
# this val can be neg. when missing == 0, begin to move the left side of the window(indicate by i).
# If  dic[s[I]] add up to 0, then stop moving left side

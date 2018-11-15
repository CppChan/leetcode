class Solution(object):
	def solution(self, height):
		lastheight= []
		for i in range(len(height)):
			h, mindif, highest= height[i], 0, True
			for j in range(len(lastheight)):
				if highest and lastheight[j]>h:
					highest = False
					mindif = j
				elif not highest and lastheight[j]>h and lastheight[mindif]-h>lastheight[j]-h: mindif = j
			if highest: lastheight.append(h)
			else: lastheight[mindif]=h
		return lastheight

if __name__=="__main__":
    s = Solution()
    print s.solution([6,5,8,3,7])
    print s.solution([5,4,3,6,2])
    print s.solution([1,1,1,1,1])
    print s.solution([6,5,8,1,1,1])
    print s.solution([5,4,6,1])
    print s.solution([4,7,9,6,5,4,2])


class Solution(object):
	def first(self, input):
		pre = None
		for i in range(len(input)):
			if not input[i].isalpha():continue
			if pre==None: pre = i
			elif ord(input[i].lower())<ord(input[pre].lower()):return i
		return None


if __name__=="__main__":
    s = Solution()
    print s.first("ba")
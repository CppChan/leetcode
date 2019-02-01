
class Solution(object):
	def finddays(self, daylist):
		max_conse, cur_conse= 0,0
		for day in daylist:
			if not self.allpresent(day): cur_conse = 0
			else:
				cur_conse+=1
				max_conse = max(max_conse, cur_conse)
		return max_conse

	def allpresent(self, day):
		for i in day:
			if i == "N": return False
		return True

s = Solution()
print s.finddays(["YYY","NNY","YYN","YYY","YYY","YYY","YNY","YYY"])
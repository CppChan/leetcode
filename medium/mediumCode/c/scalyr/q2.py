#scalyr 3
class Solution(object):
	def find(self, totalshare, input):
		input.sort(cmp = self.compare)
		dict = {}
		for person in input:
			if person[2] not in dict: dict[person[2]] = [1,person[1]]
			else:
				dict[person[2]][1]+= person[1]
				dict[person[2]][0]+=1
		dic, index= dict.items(),[0,0]
		dic.sort(key = lambda x:-x[0])
		for i in range(len(dic)):
			price, stat = dic[i][0], dic[i][1]
			if totalshare>=stat[0]:
				if totalshare<stat[1]:
					if i == len(dic)-1:return None
					index = [dic[i+1][0],0]
					break
				totalshare-=stat[1]
			else:
				index = [price, totalshare]
		for i in range(len(input)):
			if input[i][2]==index[0]:
				i+=index[1]
				return input[i][0]

	def compare(self, one, two):
		if one[2]==two[2]:return one[3]-two[3]
		return two[2]-one[2]

s = Solution()
print s.find(12,[[1,4,5,0],[2,10,6,3],[3,4,5,1],[4,4,5,2]])
class Solution(object):
	def minimumSwap(self, array):
		res = 0
		num_index = [[0]*2 for i in range(len(array))]
		for i in range(len(array)):
			num_index[i][0]=array[i]
			num_index[i][1]=i
		num_index = sorted(num_index, key=lambda x: x[0])
		visit = [False]*len(array)
		for i in range(len(num_index)):
			if num_index[i][1]==i or visit[i]:
				continue
			cyclesize = 0
			j = i
			while not visit[j]:
				visit[j]=True
				j = num_index[j][1]
				cyclesize+=1
			res+=(cyclesize-1)
		return res


#https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/


if __name__ == "__main__":
    s = Solution()
    print s.minimumSwap([2,4,5,1,3])
class Solution(object):
  def maxProfit(self, array):
  	list = [float('inf')]
  	list.extend(array)
  	list.append(-float('inf'))
  	profit = []
  	res = 0
  	stock = -1
  	for i in range(1,len(list)-1):
  		if list[i]<=list[i-1] and list[i]<list[i+1]:
  			stock = list[i]
  			profit.append(list[i])
  		elif list[i]>=list[i-1] and list[i]>list[i+1] and stock!=-1:
  			profit.append(list[i])
  			stock = -1
  	if len(profit) == 0:
  		return 0
  	byDays=[]
  	currentmin = profit[0]
  	maxprofit = 0
  	for i in range(0, len(profit)): #by ith day, how much can we get
  		currentmin = min(currentmin, profit[i])
  		maxprofit = max(maxprofit, profit[i]-currentmin)
  		byDays.append(maxprofit)
  	maxprofit = 0
  	currentmax = 0
	for i in range(len(profit)-1, -1, -1):
		currentmax = max(currentmax, profit[i])
		maxprofit = max(maxprofit, currentmax-profit[i])
		res = max(res, maxprofit+byDays[i])
	return res


if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([0,5,5,6,2,1,1,3])
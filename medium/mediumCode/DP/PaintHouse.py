class Solution(object):
  def minCost(self, costs):
    if len(costs)==0: return 0
    red,blue,green=[0]*len(costs),[0]*len(costs),[0]*len(costs)
    for i in range(len(red)):
        if len(costs[i])<3:return 0
        if i == 0:
            red[i]=costs[0][0]
            blue[i]=costs[0][1]
            green[i]=costs[0][2]
        else:
            red[i]=min(blue[i-1],green[i-1])+costs[i][0]
            blue[i]=min(red[i-1],green[i-1])+costs[i][1]
            green[i]=min(red[i-1],blue[i-1])+costs[i][2]
    return min(red[-1],blue[-1],green[-1])
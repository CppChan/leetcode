class Solution(object):
  def trap(self, distance, height):
  	wall,res = [],0
  	for i in range(len(height)-1):
  		wall.append(height[i])
  		for j in range(distance[i]):
  			wall.append(0)
  	wall.append(height[-1])
  	if len(wall)<=2:return 0
  	leftmax,rightmax= [0]*len(wall),[0]*len(wall)
  	leftmax[0],rightmax[-1]=wall[0],wall[-1]
  	for i in range(1,len(wall)):
  		leftmax[i] = max(leftmax[i-1], wall[i])
  	for j in range(len(wall)-2,-1,-1):
  		rightmax[j]= max(rightmax[j+1], wall[j])
  	tempmax = 0
  	for k in range(len(wall)):
  		waterheight = min(leftmax[k],rightmax[k])
  		if waterheight == wall[k]:
  			res= max(res, tempmax)
  			tempmax = 0
  		else:tempmax+=(waterheight-wall[k])
  	return res



if __name__ == "__main__":
    s = Solution()
    print s.trap([1,2,1,1,3,2,1,2,1],[1,0,1,0,0,0,0,0])
from collections import deque
class Solution(object):
  def find(self, input):
  	isvisit,step, queue,level = [[False]*len(input[0]) for i in range(len(input))],0, deque([(0,0)]),1
  	isvisit[0][0]=True
  	while len(queue)>0:
  		newlevel = 0
  		while level>0 and len(queue)>0:
  			node = queue.popleft()
  			if node[0]-1>=0 and not isvisit[node[0]-1][node[1]]:
  				if input[node[0]-1][node[1]]==9: return step+1
  				elif input[node[0]-1][node[1]]==0:
  					queue.append((node[0]-1, node[1]))
  					newlevel+=1
  					isvisit[node[0]-1][node[1]] = True
  			if node[0]+1<len(input) and not isvisit[node[0]+1][node[1]]:
  				if input[node[0]+1][node[1]]==9: return step+1
  				elif input[node[0]+1][node[1]]==0:
					queue.append((node[0]+1, node[1]))
					newlevel+=1
  					isvisit[node[0]+1][node[1]] = True
  			if node[1]-1>=0 and not isvisit[node[0]][node[1]-1]:
  				if input[node[0]][node[1]-1]==9:return step+1
  				elif input[node[0]][node[1]-1]==0:
  					queue.append((node[0], node[1]-1))
  					newlevel+=1
  					isvisit[node[0]][node[1]-1]=True
  			if node[1]+1<len(input[0]) and not isvisit[node[0]][node[1]+1]:
  				if input[node[0]][node[1]+1]==9:return step+1
  				elif input[node[0]][node[1]+1]==0:
  					queue.append((node[0], node[1]+1))
  					newlevel+=1
  					isvisit[node[0]][node[1]+1]=True
  			level-=1
  		step+=1
  		level = newlevel
  	return step

if __name__=="__main__":
    s = Solution()
    print s.find([[0,0,0],[1,1,0],[1,9,0]])
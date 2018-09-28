class Solution(object):
  def canWin(self, input):
  	input = list(input)
  	return self.dfs(input, True)

  def dfs(self, input, my):
  	canflip, canwin= False, False#canwin means if my can win the game
  	for i in range(len(input)-1):
  		if input[i]=="+" and input[i+1]=="+":
  			canflip = True
  			input[i],input[i+1]="-","-"
  			canwin = self.dfs(input, not my)
  			input[i],input[i+1]="+","+"
  			if canwin: break# !!! once my can win, then break loop, dont need to always win the games in every situation
  	if my and canflip and canwin:return True
  	if not my and (not canflip or canwin):return True
  	return False
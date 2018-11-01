#so efficient!!!
class Solution(object):
  def canWin(self, input):
  	if not input or len(input)<2:return False
  	for i in range(len(input)-1):
  		if input[i:i+2]=="++":
  			next=input[:i]+"--"+input[i+2:]
  			if not self.canWin(next):return True # next person cannot win 
  	return False


#wrong not pass all test case
# class Solution(object):
#   def canWin(self, input):
#   	input = list(input)
#   	return self.dfs(input, True)
#
#   def dfs(self, input, my):#my means if it is my turn
#   	canflip, canwin= False, False#canwin means if my can win the game
#   	for i in range(len(input)-1):
#   		if input[i]=="+" and input[i+1]=="+":
#   			canflip = True
#   			input[i],input[i+1]="-","-"
#   			canwin = self.dfs(input, not my)
#   			input[i],input[i+1]="+","+"
#   			if canwin: break# !!! once my can win, then break loop, dont need to always win the games in every situation
#   	if my and canflip and canwin:return True
#   	if not my and (not canflip or canwin):return True
#   	return False
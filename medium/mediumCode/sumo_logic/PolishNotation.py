class Solution(object):
  def evalPN(self, tokens):
  	stack = []
  	for i in range(len(tokens)-1, -1, -1):
  		if tokens[i].isdigit(): stack.append(int(tokens[i]))
  		elif tokens[i]=="+": stack.append(stack.pop()+stack.pop())
 		elif tokens[i] == '-':stack.append(stack.pop()-stack.pop())
 		elif tokens[i] == '*':stack.append(stack.pop()*stack.pop())
 		elif tokens[i] == '/':stack.append(stack.pop()/stack.pop())
 	return stack[0]

if __name__ == "__main__":
    s = Solution()
    print s.evalPN(["/","*","+","35","15","-","80","70", "20"])
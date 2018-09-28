# class Solution(object):
# 	def evalRPN(self, tokens):
# 		if not tokens:
# 			return 0
# 		stack = []
# 		for i in range(len(tokens)):
# 			if tokens[i] == '+':
# 				stack.append(stack.pop()+stack.pop())
# 			elif tokens[i] == '-':
# 				stack.append(-(stack.pop()-stack.pop())
# 			elif tokens[i] == '*':
# 				stack.append(stack.pop()*stack.pop())
# 			elif tokens[i] == '/':
# 			    a = stack.pop()
# 				b = stack.pop()
# 				stack.append(b/a)
# 			else:
# 				stack.append(int(tokens[i]))
# 		return stack[0]
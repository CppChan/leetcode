class Solution(object):
    def decodeString(self, s):
    	stack,i,num, pre= [],0,0, []
    	for i in range(len(s)):
    		if s[i]=="[":
    			num+=1
    			pre.append(len(stack))
    		elif s[i] == "]":
    			preindex= pre.pop()
    			j = preindex-1
    			while j>=0 and stack[j].isdigit():
    				j-=1
    			newadd = int("".join(stack[j+1:preindex])) * ("".join(stack[preindex:len(stack)]))
    			stack[j+1:]=newadd
    		else: stack.append(s[i])
    	return "".join(stack)

    #using stack
    def decodeString(self, s):
    	stack,i,pre= [],0,[]
    	while i<len(s):
    		if s[i].isdigit():
    			num = ""
    			while i<len(s) and s[i].isdigit():
    				num+=s[i]
    				i+=1
    			if len(num)>0: stack.append(num)
    			continue
    		if s[i]=="[":
    			pre.append(len(stack))
    		elif s[i] == "]":
    			preindex= pre.pop()
    			newadd = int(stack[preindex-1])*("".join(stack[preindex:len(stack)]))
    			stack[preindex-1:]=newadd
    		else:
    			stack.append(s[i])
    		i+=1
    	return "".join(stack)


if __name__=="__main__":
    s =Solution()
    s.decodeString("3[a]2[bc]")
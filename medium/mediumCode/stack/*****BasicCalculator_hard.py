def calculate(s):
    #everttune when we meet a (, we need a stack to store previous
    res, num, sign, stack = 0, 0, 1, []# res is the temp result in one ( )
    for ss in s:
        if ss.isdigit():
            num = 10*num + int(ss)# num is used for compute one number( may be 32 or 3 or 321)
        elif ss in ["-", "+"]:
            res += sign*num # compute previous sum
            num = 0
            sign = [-1, 1][ss=="+"]
        elif ss == "(":
            stack.append(res) # store it for future use
            stack.append(sign)
            sign, res = 1, 0#new res
        elif ss == ")":
            res += sign*num# jiesuan the value in ()
            res *= stack.pop() # value in () * sign
            res += stack.pop()
            num = 0 # here is very very very important! because next round we wont compute previous sum
    return res + num*sign


print calculate("2-(5-(6-2))")
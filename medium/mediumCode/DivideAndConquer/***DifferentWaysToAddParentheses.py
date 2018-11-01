class Solution(object):
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i in xrange(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        return res
    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n

# class Solution(object):
#     def diffWaysToCompute(self, input):
#         return sorted(self.compute(input))
#
#     def compute(self, input):
#         if len(input) == 0: return []
#         if len(input) == 1: return [int(input[0])]
#         res = []
#         for i in range(len(input) - 2):#here is -2 because we dont need to consider the whole input(not kuohao's situation)
#             if input[i] in "+-*": continue
#             temp1 = self.compute(input[0:i + 1])
#             temp2, fuhao = [], '+'#remember the ''
#             if i < len(input) - 1:
#                 temp2 = self.compute(input[i + 2:len(input)])
#                 fuhao = input[i + 1]
#             res.extend(self.addup(temp1, temp2, fuhao))
#         return res
#
#     def addup(self, temp1, temp2, fuhao):
#         if len(temp2) == 0: return temp1
#         res = []
#         for i in temp1:
#             for j in temp2:
#                 if fuhao == "+":
#                     res.append(i + j)
#                 elif fuhao == "-":
#                     res.append(i - j)
#                 elif fuhao == "*":
#                     res.append(i * j)
#         return res
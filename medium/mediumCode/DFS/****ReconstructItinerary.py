class Solution(object):
    def findItinerary(self, tickets):
        if len(tickets) == 1: return tickets[0]
        dic = {}
        tickets = sorted(tickets, cmp=self.comp)
        for i in range(len(tickets)):
            if not dic.has_key(tickets[i][0]):
                dic[tickets[i][0]] = [tickets[i][1]]
            else:
                dic[tickets[i][0]].append(tickets[i][1])
        res = ['JFK']
        self.formtrip(dic, 'JFK', res, len(tickets) + 1)
        return res

    def comp(self, x, y):
        if len(x) == 1 and len(y) == 1:
            if x[0] == y[0]:
                return 0
            else:
                return cmp(x[0], y[0])
        elif x[0] == y[0]:
            return self.comp([x[1]], [y[1]])
        else:
            return cmp(x[0], y[0])

    def formtrip(self, dic, pos, res, num):
        if num == 1: return True
        if pos not in dic: return False
        dests = dic[pos]
        for i in range(len(dests)):
            if dests[i][-1] != "*":
                ori = dests[i]
                dests[i] = dests[i] + "*"
                res.append(ori)
                if self.formtrip(dic, ori, res, num - 1):
                    return True
                else:
                    dests[i] = ori
                    res.pop(-1)
        return False


s = Solution()
s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])

    # def formtrip(self, dic, pos, res, num):
    #     if not dic.has_key(pos):
    #         if len(res) == num:
    #             return True
    #         else:
    #             return False
    #     for i in range(len(dic[pos])):
    #         item = dic[pos][i]
    #         res.append(item)
    #         dic[pos].pop(i)
    #         if not self.formtrip(dic, item, res, num):#backtracking
    #             dic[pos].insert(i, item)
    #             res.pop(-1)
    #         else:
    #             break
    #     if len(res) < num:
    #         return False
    #     else:
    #         return True
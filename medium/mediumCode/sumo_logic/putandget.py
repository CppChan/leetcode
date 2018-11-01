class Solution(object):
    dic = {}
    def __init__(self, name, year, location):
        self.dic[(name,year)] = location

    def put(self, name, year, location):
        self.dic[(name,year)] = location

    def getyear(self, name, year):
        if (name, year) not in self.dic:
            closest,itemlist,res = float('inf'),self.dic.items(),""
            for item in itemlist:
                if abs(item[0][1]-year)<closest:
                    closest = abs(item[0][1]-year)
                    res = self.dic[item[0]]
            return res
        else:return self.dic[(name, year)]




if __name__ == "__main__":
    s = Solution('xijia',1995,'a')
    s.put('chen',1994,'a')
    s.put('bao',1996,'g')
    s.put('luo',1998,'q')
    print s.getyear('ss',1992)
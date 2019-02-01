class Solution(object):
    def findDuplicate(self, paths):
        dic = {}
        for i in range(len(paths)):
            info = paths[i].split(" ")
            for j in range(1, len(info)):
                txt = info[j]
                txt_info = txt.split("(")
                if txt_info[1] in dic: dic[txt_info[1]].append(info[0]+"/"+txt_info[0])
                else: dic[txt_info[1]]=[info[0]+"/"+txt_info[0]]
        res = []
        dic = dic.items()
        for i in range(len(dic)):
            if len(dic[i][1])>1:res.append(dic[i][1])
        return res
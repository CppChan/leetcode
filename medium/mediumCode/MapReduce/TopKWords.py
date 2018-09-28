class MR1(object):
    def mapper(self, array):#used for word count
        mapOutput = []
        for item in array:
            temp = (item,1)
            mapOutput.append(temp)
        return mapOutput

    def reducer(self, mapOutput):
        dict = {}
        for item in mapOutput:
            if item[0] not in dict:
                dict[item[0]] = 1
            else:
                dict[item[0]]+=1
        return dict

class MR2(object):#used for sorting

    def mapper(self, dict):
        list = dict.iteritems()#each item is word:count
        res = {0:[],1:[],2:[]}#each represent range
        for item in list:
            if item[1]>0 and item[1]<=5:
                res[2].append(item)
            elif item[1]>5 and item[1]<=10:
                res[1].append(item)
            elif item[1] > 10 and item[1] <= 15:
                res[0].append(item)
        return res

    def reducer(self, dict, k):
        list = dict.iteritems()#each item is range:[(word, count)]
        res = []
        count = 0
        for item in list:
            rangeData = item[1]
            rangeData = sorted(rangeData, key = lambda x:-x[1])
            if count+len(rangeData)>k:
                for i in range(k-count):
                    res.append(rangeData[i])
                break
            else:
                res.extend(rangeData)
                count+=len(rangeData)
        return res


if __name__ == "__main__":
    array = ["apple","apple","apple","apple","apple",
             "pair", "pair","pair","pair","pair","pair","pair","pair",
             "water", "water","water","water","water","water","water","water","water","water","water",
             "chicken", "chicken","chicken","chicken",
             "banana","banana","banana","banana","banana","banana","banana","banana","banana","banana","banana","banana",
             "orange","orange"]
    # array.index()
    mr1 = MR1()
    mr2 = MR2()
    temp = mr1.mapper(array)
    dict1 = mr1.reducer(temp)
    dict2 = mr2.mapper(dict1)
    print mr2.reducer(dict2, 4)





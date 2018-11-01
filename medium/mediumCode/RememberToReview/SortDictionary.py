from collections import OrderedDict
from collections import defaultdict

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Student(object):
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class Solution(object):

    def defaultdicttest(self):
        d = defaultdict(lambda : 0)
        d[0]+=1
        print d[0]

    def removekey(self):
        dic = {'a':1,'b':2}
        dic.__delitem__('a')
        print dic

        list = set([1,2,3])
        list.add(4)
        list.remove(3)
        print list

    def percentile95(self, lengths):

        dic = {}
        for i in range(1, 4097):
            dic[i] = 0
        for j in lengths:
            dic[j] += 1
        nums = 0
        for item in dic.iteritems():
            if item[1]!= 0:
                nums += item[1]
            if nums >= len(lengths) * 0.95:
                return item[0]

    def sortDicAccordingToKey(self):
        dic = {}
        s1 = Student('chen', 105)
        s2 = Student('xi', 101)
        s3 = Student('jia', 102)
        dic[(s1.name, s1.grade)] = s1.grade
        dic[(s2.name, s2.grade)] = s2.grade
        dic[(s3.name, s3.grade)] = s3.grade
        print dic.iteritems()
        print sorted(dic.iteritems(), key=lambda d:d[0][0], reverse = True)#method 1 according to key, dic.iteritems() is tuple!!!!!,SO
        #overall is a tupleSet


        keySet = dic.keys()
        keySet.sort(key = lambda student: student[1])#method2 according to key
        print [dic[key] for key in keySet]

    def sortDicAccordingTovalue(self):
        dic = {}
        s1 = Student('chen', 105)
        s2 = Student('xi', 101)
        s3 = Student('jia', 102)
        dic[s1.name] = s1.grade
        dic[s2.name] = s2.grade
        dic[s3.name] = s3.grade
        print sorted(dic.iteritems(), key=lambda d: d[1], reverse=True)

    def orderedDicImplementation(self):#maintain insert order
        orderDic = OrderedDict()
        s1 = Student('chen', 105)
        s2 = Student('xi', 101)
        s3 = Student('jia', 102)
        orderDic[(s2.name, s2.grade)] = s2.grade
        orderDic[(s1.name, s1.grade)] = s1.grade
        orderDic[(s3.name, s3.grade)] = s3.grade
        print orderDic


if __name__ == "__main__":
    s = Solution()
    s.defaultdicttest()
    s.removekey()
    print("***********************")
    print s.percentile95([1,2,3,4,5,6,7,8,9,10])
    print("***********************")
    s.sortDicAccordingToKey()
    print("***********************")
    s.sortDicAccordingTovalue()
    print("***********************")
    s.orderedDicImplementation()
    print("***********************")


    #test: difference between java and python!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    a = (1,2)
    b = (1,2)
    dic = {a:1, (2,3):2}
    print dic.has_key(b)#True because tuple is unchangable object in python, btw, list is unhashable in python

    c = TreeNode(1)
    d = TreeNode(1)
    dic2 = {c:1, (2,3):2}
    print dic.has_key(d)#False


    # In java!!!!!!!!


    # class TestHash {
    #     public static void main(String[] args) {
    #         HashMap < String, Integer > map = new HashMap < String, Integer > ();
    #         String a = "12";
    #         String b = "12";
    #         map.put(a, 1);
    #         System.out.print(map.containsKey(b)); #True
    #
    #
    #         tuple c = new tuple(1, 2);
    #         tuple d = new tuple(1, 2);
    #         HashMap < tuple, Integer > map2 = new HashMap < tuple, Integer > ();
    #         map2.put(c, 1);
    #         System.out.print(map2.containsKey(d)); #False
    #     }
    # }
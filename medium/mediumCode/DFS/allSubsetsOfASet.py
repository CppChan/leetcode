class Solution(object):
    def findSubsets1(self, array):
        res = []
        if len(array)==0:
            res.append('')
            print res
        else:
            self.helper(array, res, 0, 0)
            res.append([])
            print res

    def helper(self, array, res, begin, last):
        if len(res)==0:
            for i in range(len(array)):
                res.append(array[i])
                self.helper(array, res, i+1,len(res)-1)
        else:
            for i in range(begin,len(array)):
                res.append(res[last]+(array[i]))
                self.helper(array, res, i+1,len(res)-1)

    def findSubsets2(self, array):
        if not array:
            return ['']
        else:
            r = self.findSubsets2(array[:-1])
            k = len(r) # in java, must do that, because len(r) will change as the r grow
            for i in range(k):
                r.append(r[i] + array[-1])
            return r

    def findSubsets3(self, array):#see eclipse DFS directory
        return


if __name__=='__main__':
    # array1 = ['a', 'b', 'c','d']
    # array2 = ['a', 'b', 'c','d']
    # s = Solution()
    # s.findSubsets1(array1)
    # res = s.findSubsets2(array2)
    # print res
    a = []
    a.append(1)

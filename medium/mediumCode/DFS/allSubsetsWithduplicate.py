class Solution(object):
    def findSubsets1(self, input): # from laidata
        res = []
        self.helper2(input, 0, [], res)
        print res

    def helper2(self, input, index, solution, res):
        if index == len(input):
            res.append(solution[:])
            return
        solution.append(input[index])
        self.helper2(input, index+1, solution, res)
        solution.pop()
        i = index
        while i <len(input) and input[index] == input[i]:
            i+=1
        self.helper2(input, i, solution, res)

    def findSubsets2(self, S):#more prefer!!!!!
        res = [[]]
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res

    def findSubsets3(self, array):
        res = []
        self.helper(array, res, 0, 0)
        res.append([])
        print res

    def helper1(self, array, res, start, end):
        if len(res)==0:
            for i in range(len(array)):
                if i == 0 or (i>0 and array[i]!=array[i-1]):
                    res.append(array[i])
                    self.helper1(array, res, i+1,len(res)-1)
        else:
            for i in range(start,len(array)):
                if array[i]!=array[i-1] or i == start:
                    res.append(res[end]+(array[i]))
                    self.helper1(array, res, i+1,len(res)-1)
                else:
                    continue


    def findSubsets4(self, array):#in eclipse , DFS allSUBSETS
        return



if __name__ == "__main__":
    s = Solution()
    # s.find('abbc')
    s.findSubsets1('abbc')
    # print s.findSubsets2('abbc')
    # print res
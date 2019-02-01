import itertools
import collections



#method 1
# shortest path algorithm ---Floyd algorithm

# https://www.cnblogs.com/George1994/p/7237473.html

def calcEquation(self, equations, values, queries):
    quot = collections.defaultdict(dict)
    for (num, den), val in zip(equations, values):
        quot[num][num] = quot[den][den] = 1.0
        quot[num][den] = val
        quot[den][num] = 1 / val
    for k in quot:
        for i in quot[k]:
            for j in quot[k]:
                quot[i][j] = quot[i][k] * quot[k][j]
    return [quot[num].get(den, -1.0) for num, den in queries]

# for k, i, j in itertools.permutations(['a','b','c','d','e'],3):
#     print k, i, j



# calcEquation([ ["a", "b"], ["b", "c"] ],[2.0, 3.0],[ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ])



#method 2


# in letter={}  a:[b,3] means a/b = 3 and b is the parent of a(!!!not the root, only parent)
#                                                   1/c1_value   *    value     *  c2_value
# in the example, first a---->b , then b ---> d = b------------>a------------->d----------->d
#
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        def find(letters, c): #find how far to the root
            value = 1.0
            while c != letters[c][0]:
                value *= letters[c][1]
                c = letters[c][0]
            # print(c, value)
            return [c, value]#find the root

        def union(letters, c1, c2, value):
            c1_root, c1_value = find(letters, c1)
            c2_root, c2_value = find(letters, c2)
            letters[c1_root] = [c2_root, value * c2_value / c1_value]

        letters = {}
        for l1, l2 in equations: # initialize every node's root is itself
            letters[l1] = [l1, 1.0]
            letters[l2] = [l2, 1.0]
        # print(letters)
        for i in range(len(equations)):
            union(letters, equations[i][0], equations[i][1], values[i])
        # print(letters)
        ans = []
        for q1, q2 in queries:
            if q1 not in letters or q2 not in letters:
                ans.append(-1.0)
                continue
            q1_root, q1_value = find(letters, q1)
            q2_root, q2_value = find(letters, q2)
            # print(q1_root, q1_value, q2_root, q2_value)
            if q1_root != q2_root:# in each cluster, there will be one root
                ans.append(-1.0)
            else:
                ans.append(q1_value / q2_value)
        return ans


if __name__=="__main__":
    s =Solution()
    s.calcEquation([ ["a", "b"],["a","d"], ["b", "c"] ],[5.0, 2.0, 3.0],[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
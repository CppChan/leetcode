class Solution(object):
    def read(self):
        res = []
        with open('./input.txt','r') as f:
            for line in f.readlines():
                res.append(line.strip())
            for line in res:
                temp = line.split(" ")
                print temp
        print res
    def write(self):
        with open("./output.txt",'w') as f:
            f.write('I like climbing\n')
            f.write('I like football')

if __name__ == "__main__":
    s = Solution()
    s.read()
    s.write()
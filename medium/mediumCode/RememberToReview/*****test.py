class solution(object):
    list = [0,1,2]
    def change(self):
        new1 = self.list
        # new1[0]=10
        self.change2()
        new2 = self.list
        print new1[0]
        print new2[0]
    def change2(self):
        newlist = [10,2,4]
        self.list = newlist#list refer to a new object, but new1 still refer to its previous version !!!!!!!!!

if __name__ == "__main__":
    print min(1,2,3,3)

    for i in range(10,-1,-1):# first two num is range, remember to add last -1 indicated direction
        print i

    array = [3,5,2,5,6]
    #two ways to sort
    array = sorted(array)
    array.sort()#1
    print array

    array = sorted(array)#2
    s = solution()
    s.change()


    a = "123"
    b = int(a)

    print("*******")

    print cmp("sd","dsfds")

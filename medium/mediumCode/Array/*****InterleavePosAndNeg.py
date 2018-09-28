class Solution(object):
  def interleave(self, array):
    pos,neg = 0, 0
    if len(array)<2: return array
    for i in range(len(array)):
        if array[i]>0:pos+=1
        elif array[i]<0: neg+=1
    if pos!=neg:
        self.move1(array, pos,neg)
    i,j = 0, 1
    while i<len(array)-abs(pos-neg) and j<len(array)-abs(pos-neg):#abs!!!!!
        if array[i]<0 and array[j]>0:
            temp = array[i]
            array[i]=array[j]
            array[j] = temp
            i+=2
            j+=2
        elif array[i]<0:j+=2
        elif array[j]>0:i+=2
        else:
            i+=2
            j+=2
    return array


  def move1(self,array, pos, neg):
    diff,i,j = abs(pos-neg),0,len(array)-1
    if pos>neg:
        i=1
        while j>len(array)-diff-1:
            if array[j]>0:j-=1
            else:
                while array[i]<0:i+=2
                temp = array[i]
                array[i]=array[j]
                array[j] = temp
                j-=1
    else:
        i=0
        while j>len(array)-diff-1:
            if array[j]<0:j-=1
            else:
                while array[i]>0:i+=2
                temp = array[i]
                array[i]=array[j]
                array[j] = temp
                j-=1
if __name__ == "__main__":
    s = Solution()
    s.interleave([-1,-1,-1,-1,1,-1,1,-1,-1])
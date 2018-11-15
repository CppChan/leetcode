class Solution(object):
    def numberToWords(self, num):
        if num==0:return "Zero"
        num = str(num)
        word,i,res= ['','Thousand','Million','Billion'],len(num)-1,''
        while i>=0:
            temp= self.transfer(num[max(i-2,0):i+1])+" "+word[(len(num)-1-i)/3]
            if word[(len(num)-1-i)/3]>0:temp=temp+" "
            i-=3
            res = temp+res
        for i in range(len(res)-1,-1,-1):
            if res[-1]!=" ":break
        return res[:i+1]
    def transfer(self, num):
        w1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        w2 = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        if len(num)==1:return w1[int(num)]
        backtwo,res= num[len(num)-2:],""
        if int(backtwo)>=20:
            res = w2[int(num[(len(num)-2):(len(num)-1)])]+" "+w1[int(num[-1])]
        else:res = w1[int(backtwo)]
        if len(num)==3:
            if num[0]=="0":return res
            res = w1[int(num[0])]+" Hundred "+res
        return res

if __name__=="__main__":
    s = Solution()
    print s.numberToWords(123)[-3]
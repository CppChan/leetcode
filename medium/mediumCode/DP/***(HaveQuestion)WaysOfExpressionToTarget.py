class Solution(object):
  def ways(self, exp, target):
    if len(exp)==0: return 0
    if len(exp)==1:
        if int(exp[0])==target:return 1
        else: return 0
    dp1 = [0]*(((len(exp)-1)/2)+1)
    dp0 = [0]*(((len(exp)-1)/2)+1)
    if exp[0]=='0':dp1[0], dp0[0]=0,1
    elif exp[0]=='1':dp1[0],dp0[0]=1,0
    dpi = 1
    for i in range(2, len(exp), 2):
        istarget = 0
        temp = int(exp[i])
        for j in range(i, 1, -2):
            if j == 2 :
                temp = self.judge(temp,exp[1],int(exp[0]))
                if temp == target:
                    istarget+=1
                if target == 1:dp1[dpi],dp0[dpi]=istarget,1-istarget
                elif target ==0:dp0[dpi],dp1[dpi]=istarget,1-istarget
            else:
                if target == 1:
                    if temp ==1 and exp[j-1]=='&': istarget+=dp1[(j-1)/2]
                    elif temp ==1 and exp[j-1]=='^': istarget+=dp0[(j-1)/2]
                    elif temp == 1 and exp[j-1]=='|': istarget+=dp0[(j-1)/2]+dp1[(j-1)/2]
                    elif temp ==0 and exp[j-1]=='&': istarget+=0
                    elif temp ==0 and exp[j-1]=='^': istarget+=dp1[(j-1)/2]
                    elif temp == 0 and exp[j-1]=='|': istarget+=dp1[(j-1)/2]
                    dp1[dpi]=istarget
                elif target == 0:
                    if temp ==1 and exp[j-1]=='&': istarget+=dp0[(j-1)/2]
                    elif temp ==1 and exp[j-1]=='^': istarget+=dp1[(j-1)/2]
                    elif temp == 1 and exp[j-1]=='|': istarget+=0
                    elif temp ==0 and exp[j-1]=='&': istarget+=dp0[(j-1)/2]+dp1[(j-3)/2]
                    elif temp ==0 and exp[j-1]=='^': istarget+=dp0[(j-1)/2]
                    elif temp == 0 and exp[j-1]=='|': istarget+=dp0[(j-1)/2]
                    dp0[dpi]=istarget
                temp = self.judge(temp, exp[j-1],int(exp[j-2]))
        dpi+=1
    if target == 1: return dp1[len(dp1)-1]
    else: return dp0[len(dp0)-1]

  def judge(self, temp, fuhao, temp2):
    if fuhao=='&':
        if temp==1 and temp2==1: return 1
        else: return 0
    elif fuhao == '|':
        if temp==0 and temp2 == 0: return 0
        else: return 1
    elif fuhao == '^':
        if temp!=temp2: return 1
        else: return 0


if __name__ == "__main__":
    s =Solution()
    print s.ways(["0","&","1","|","1"],1)
import sys
def findsmallest(input):
    sum = 0
    for i in range(len(input)):
        input[i]=int(input[i])
        sum+=input[i]
    bitmap = [0]*sum
    for i in range(1,len(input)+1):
        dfs(bitmap,input, i, 0,0)
    for i in range(len(bitmap)):
        if bitmap[i]==0:return i+1
    return len(bitmap)+1
def dfs(bitmap, input, length, i, pre):
    if length==0:
        if bitmap[pre-1]==0:bitmap[pre-1]=1
        return
    for i in range(i, len(input)-length+1):
        dfs(bitmap, input, length-1, i+1, pre+input[i])

if __name__=="__main__":
    n = int(sys.stdin.readline().strip())
    input = sys.stdin.readline().strip()
    input = input.split(" ")
    print findsmallest(input)
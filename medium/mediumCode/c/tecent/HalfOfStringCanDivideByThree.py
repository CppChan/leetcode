def find(input):
    dic_set,res,dp = [[{}]*len(input) for i in range(len(input))],0, [[0]*len(input) for i in range(len(input))]
    for k in range(len(input)):
        for i in range(len(input)-k):
            j = i+k
            if i == j:
                dic_set[i][j]={finddivide(input[i]):1}
                dp[i][j]=1
            else:
                dic1,dic2, i_count, j_count = dic_set[i+1][j],dic_set[i][j-1],finddivide(input[i]),finddivide(input[j])
                dict = dic1.copy()
                if i_count in dict:dict[i_count]+=1
                else: dict[i_count]=1
                dp[i][j] = max(max(dp[i+1][j], dict[i_count]), max(dp[i][j-1],dict[j_count]))
                dic_set[i][j]= dict
                if dp[i][j]>=(j-i+1)/2: res = max(res, j-i+1)
    return res
def finddivide(k):
    for i in range(2,k+1):
        if k%i==0:return i


if __name__=="__main__":
    # n = int(sys.stdin.readline().strip())
    # input = sys.stdin.readline().strip()
    # input = input.split(" ")
    # for i in range(len(input)):
    #     input[i]=int(input[i])
    print find([8,8,5,5,4,7,3,11])

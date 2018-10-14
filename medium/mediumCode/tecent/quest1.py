
def findstring(input, n):
    res,i,j,temp_count = 0,0,0,0
    while j<len(input) and i<=j:
        while temp_count<n and j<len(input):
            if input[j]=="1":temp_count+=1
            j+=1
        i_count,j_count = 1,1
        while j<len(input) and input[j]=='0':
            j+=1
            j_count+=1
        while i<j and input[i]=="0":
            i+=1
            i_count+=1
        res += (i_count) * (j_count)
        i+=1
        temp_count-=1
    return res

if __name__=="__main__":
    print findstring("110111", 2)
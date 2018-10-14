def mean(two_d_array):
    if len(two_d_array)==0:return []
    res = []
    for i in range(len(two_d_array)):
        res.append(comp_avg(two_d_array[i]))
    return res
def comp_avg(input):
    info = get_sum(input)
    res = float(info[0])/float(info[1])
    str_res = str(res).split('.')
    if len(str_res[1]) == 1 and str_res[1][0]=='0': return int(res)
    return float('%.1f'%res)
def get_sum(input):
    count, sum_ = 0,0
    for i in range(len(input)):
        if input[i]!=0:
            count+=1
            sum_+=input[i]
    return (sum_, count)

if __name__ == "__main__":
    print comp_avg([-1,2,0])
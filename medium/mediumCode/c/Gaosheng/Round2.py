
def export_result(num):
    num_x , num_y = str(num).split('.')
    num = float(num_x+'.'+num_y[0:2])
    return num

if __name__=="__main__":
    a = 2
    b = 3
    print(format(float(a)/float(b), '.2f'))
    print export_result(float(a)/float(b))
    print "a".upper()
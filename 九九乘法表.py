for i in range(1,10):     # 外层循环，从1到9
    for j in range(1,i+1):      # 内层循环，从1到当前的i
        print("%dx%d=%d\t"%(j,i,i*j),end='')    # 打印乘法结果，使用end=''不换行
    print()
print()

for i in range(9,-1,-1):    # 外层循环，从9到0（包括0）
    for j in range(1,i+1):    
        print("%dx%d=%d\t"%(j,i,i*j),end='')
    print()
    


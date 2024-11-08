sum=0     # 素数计数器
for j in range(2,1001):
    flag=1               # 标志位，假设当前数j是素数
    a=j
    for i in range(2,a):   #2 到 j-1 的所有数 i，检查 j 是否能被 i 整除。
        if(a%i==0):        #如果 j 能被 i 整除（余数为 0），说明 j 不是素数
            flag=0
            break           # 立即退出内层循环
    if (flag==1):           # 如果 flag 仍为 1，说明 j 是素数
        sum=sum+1           # 素数计数器加 1
        print ("素数有%d\t"%j)     # 输出素数 j       
print("素数的总数为:",sum)        


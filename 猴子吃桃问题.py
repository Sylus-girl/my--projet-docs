sum=1
print("小猴子在第10天时，桃子数为1个")
for i in range(9,0,-1):        #从9天到1天（包括9，但不包括0），步长为-1
    sum=(sum+1)*2
    print("小猴子在第{}天时，桃子数为{}个".format(i,sum))

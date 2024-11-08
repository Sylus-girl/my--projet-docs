from math import sqrt
def prime(n):
     flag=1
     if n>1 :      
                    
         
         for i in range(2, int(sqrt(n) + 1)):   #从2开始，依次检查n是否能被2到sqrt(n)之间的整数整除。
             if(n%i==0):      
                flag=0          #如果可以整除，则flag变为0，函数返回0，表示n不是素数。
                return 0
             else:
               print("%d"%i,end='')
               return 1               #函数返回1，表示n是素数
               
sum=0
for i in range(1,10):
    if prime(i):
         print("%d"%i,end='')
         sum+=prime(i)                    #调用prime(i)函数，判断i是否为素数
                                #如果是（返回值为1），就将其加入primes列表。

                                          #将所有的素数转为字符串形式，并使用逗号连接，输出所有找到的素数。
print("素数有: ",sum,"个")   #输出素数的个数
    
     

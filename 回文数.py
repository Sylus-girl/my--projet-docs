a=[]                 # 用于存储回文数的列表

def back(j):        #将数字拆分成个位、十位、百位、千位、万位


    b=j%10           # 个位
    c=int(j/10%10)   # 十位
    d=int(j/10/10%10) # 百位
    e=int(j/10/10/10%10) # 千位
    f=int(j/10/10/10/10%10) # 万位

    if b==f and c==e:   #判断是否为回文数
       
        a.append(j)    # 将回文数添加到列表中

        return 1        # 返回1表示找到一个回文数


    else:
        return 0        # 返回0表示不是回文数
sum=0                                       
for i in range(10000,100000):
    sum=sum+back(i)     # 累加回文数的数量
print("",a)
print("回文数总数为：",sum)




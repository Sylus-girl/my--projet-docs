sum=0     # 用于记录玫瑰花数的总数
for i in range(1000,10000):
    flag=1
    b=i%10  # 个位
    c=int(i/10%10)  # 十位
    d=int(i/10/10%10)   # 百位
    e=int(i/10/10/10%10)   # 千位
    if(b**4)+(c**4)+(d**4)+(e**4)==i:   # 判断是否为玫瑰花数
        flag=1
        print("",i)      # 输出这个玫瑰花数
        sum=sum+1        # 计数加1
    else:
        flag=0
print("玫瑰花总数为：",sum)
    
    
    
    

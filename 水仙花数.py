def back(n):
        b=n%10    #个位
        c=int(n/10%10)  #十位
        d=int(n/10/10%10)   #百位
        if n==(b**3)+(c**3)+(d**3):
            print("",n)
            return 1    #是水仙花数，输出并返回 1，表示找到一个水仙花数
        else:
            return 0    #返回 0，表示 n 不是水仙花数

sum=0
for i in range(100,1000):
        sum=sum+back(i)

print("水仙花数总数为：",sum)
     
    
    

        
    

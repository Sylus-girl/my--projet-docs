a=str(input("请输入密码："))

m=[]      # m 用于存储密文
k=[]     # k 用于存储明文

def jiami(a):
    for i in a:         # i遍历a中的每一个字符
            b=ord(i)    #字符 i 转换为其对应的整数
            if b==7 or b==8 or b==9:   #特殊情况另外处理
                b=b-7
            elif  b==88 or b==89 or b==90 or b==120 or b==121 or b==122:
                b=b-23
            else:
                b=b+3        #对于其他字符，加 3，来实现加密
            d=chr(b)         #chr() 将修改后的整数转换回字符，存储在 d 中
            m.append(d)
           
    
def jiemi(a):
      for j in a:
             e=ord(j)
             if e==48 or e==49 or e==50:
                 e=e+7
             elif e==97 or e==98 or e==99:
                 e=e+23
             else:
                e=e-3
             f=chr(e)
            
             k.append(f) 

p="y"               #假设 p 为 "y"，进入一个循环，只要 p 为 "y" 就不断执行。
while(p=="y"):
    c=input("你要加密还是解密呢？1加密，2解密")
    if(int(c)==1):
        jiami(a)
        print("加密后的密文为:"+"".join(m))
    if(int(c)==2):
        jiemi(a)
        print("解密后的明文为:"+"".join(k))
    p=input("想再玩一次吗,想-y,不想-n")


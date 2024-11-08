import datetime
a=datetime.datetime.now()
print(a)
while(1):
    print("尚品坊购物中心(欢迎光临）")
    print("\n请输入品名：")
    p=input()
    print("\n请输入数量：")
    s=input()
    s=int(s)
    print("\n请输入单价：")
    d=input()
    d=float(d)
    xj=s*d
    print("品名为:",p,"数量:",s,"单价：",d,"小计：",xj)
    print("\n请输入品名：")
    c=input()
    print("\n请输入数量：")
    b=input()
    b=int(b)
    print("\n请输入单价：")
    e=input()
    e=float(e)
    xg=b*e
    print("品名为:",c,"数量:",b,"单价：",e,"小计：",xg)
    print("\n请输入品名：")
    r=input()
    print("\n请输入数量：")
    t=input()
    t=int(t)
    print("\n请输入单价：")
    u=input()
    u=float(u)
    hg=t*u
    print("品名为:",r,"数量:",t,"单价：",u,"小计：",hg)
    w=xj+xg+hg
    print("==============================================")
    print("尚品坊购物中心(谢谢惠顾)")
    print("柜台：749   收银员：小明")
    print("票号：57849454")
    print("----------------------------------------------")
    print("合计：",w,)
    print("支付方式：支付宝")
    f=300-w
    print("实付:300.00"," 找零：",f,)
    print("==============================================")
    



    

    
    
    

def get_bmi():
    w=float(input("请输入体重：（kg）"))#保存身高的变量，单位：米
    h=float(input("请输入身高：（m）")) #保存体重的变量，单位：千克
    bmi=w/(h*h)                         #用于计算BMI指数，公式为：“体重/身高的平方”
    return bmi
def jud(x):
    if (x<18):
        print("长得像枯猴哦")
        print("不要挑食哦")
    elif (18<x<=24):
        print("刚刚好")
        print("加油！保持住！")
    elif(x<=28):
        print("小肚腩")
        print("管住嘴，多运动")
    else:
        print("胖墩哦")
        print("小心三高哦！")

an="y"
while(an=="y"):             #循环控制语句
    zs=get_bmi()
    print("你的肥胖指数为%.2f"%zs)     #输出BMI指数 %转义字符
    jud(zs)
    an=input("你想再测一次吗？（y\n）")
    

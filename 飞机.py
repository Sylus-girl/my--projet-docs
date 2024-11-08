import turtle as t                  #导入 Turtle 库
t.speed(0)


date1=[250,200,50]                  #date1 定义了第一个圆的中心坐标和半径
date2=[-300,150,6,-16,-300,150,-115,-85]   #一组坐标和线段长度
date3=[412,111,335,128,50,316,350,100,70]   #一系列线段的长度

def yuan(x,y,z):                    #定义yuan 的函数，绘制一个太阳。
    t.seth(0)
    t.color("red")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(z)
    t.end_fill()

yuan(date1[0],date1[1],date1[2])
t.hideturtle()


t.seth(-14)
t.color("blue")                     #绘制蓝色形状
t.penup()
t.goto(date2[0],date2[1])
t.pendown()
t.begin_fill()
t.forward(date3[0])
t.right(130)
t.forward(date3[1])
t.right(64)
t.forward(date3[2])
t.end_fill()

t.penup()                       #绘制额外的黑色线条
t.goto(date2[2],date2[3])
t.pensize(5)
t.color("black")
t.seth(-120)
t.pendown()
t.forward(date3[3])
t.right(130)
t.forward(date3[4])
t.left(24)
t.forward(date3[5])




t.penup()                       #绘制第二个蓝色形状
t.goto(date2[4],date2[5])
t.pendown()
t.seth(-12)
t.color("blue")
t.begin_fill()
t.right(50)
t.forward(date3[6])
t.left(120)
t.forward(date3[7])
t.end_fill()

t.penup()                       #绘制最后一个蓝色线条
t.goto(date2[6],date2[7])
t.pendown()
t.seth(-40)
t.color("blue")
t.forward(date3[8])






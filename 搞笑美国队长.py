import turtle as t
t.speed(0)

def yuan1(x,y,z):           #yuan1 函数用于绘制红色的大圆，x 和 y 为圆心，z 为半径
    t.seth(0)
    t.color("red")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(z)
    t.end_fill()


yuan1(-200,-200,200)

def yuan2(a,b,c):           #yuan2 函数用于在红色圆的内部绘制一个白色圆。
    t.seth(0)
    t.color("white")
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.begin_fill()
    t.circle(c)
    t.end_fill()

yuan2(-200,-170,170)
yuan1(-200,-130,130)

def yuan3(d,e,f):           #yuan3 函数用于绘制蓝色的小圆
    t.seth(0)
    t.color("blue")
    t.penup()
    t.goto(d,e)
    t.pendown()
    t.begin_fill()
    t.circle(f)
    t.end_fill()
yuan3(-200,-90,90)



def eye(a,b):               #eye 函数用于绘制眼睛。先绘制棕色圆，再绘制内部白色圆
    t.seth(0)
    t.color("brown")
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.circle(35)
    t.begin_fill()
    t.color("white")
    t.circle(35)
    t.end_fill()
    t.hideturtle()


def eyeball1(c,d,l,p):      #eyeball1 函数用于绘制黑色的瞳孔，l 为半径，p 为角度
    t.seth(0)
    t.color("black")
    t.penup()
    t.goto(c,d)
    t.pendown()
    t.begin_fill()
    t.circle(l,p)
    t.end_fill()
    t.hideturtle()



def mouth(e,f,m,n):     #mouth 函数用于绘制嘴巴，通过绘制两条弧线形成一个微笑的效果
    t.seth(0)
    t.color("white")
    t.penup()
    t.goto(e,f)
    t.pendown()
    t.circle(m,n)


    



eye(-300,30)
eye(-125,30)
eyeball1(-300,30,25,360)
eyeball1(-125,30,25,360)
mouth(-200,-80,100,30)
mouth(-200,-80,100,-30)













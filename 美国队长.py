import turtle as t
t.speed(0)

def yuan1(x,y,z):               #yuan1 函数用于绘制一个红色的圆形
    t.seth(0)
    t.color("red")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(z)
    t.end_fill()


yuan1(-200,-200,200)

def yuan2(a,b,c):               #yuan2 函数用于绘制一个白色的圆形
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

def yuan3(d,e,f):               #yuan3 函数用于绘制蓝色的小圆
    t.seth(0)
    t.color("blue")
    t.penup()
    t.goto(d,e)
    t.pendown()
    t.begin_fill()
    t.circle(f)
    t.end_fill()
yuan3(-200,-90,90)

t.penup()
t.goto(-290,23)                 #移动，准备绘制星形图案
t.color("white")
t.begin_fill()
for i in range(4):
    t.forward(177)
    t.right(144)
t.end_fill()
t.hideturtle()















import turtle as t
t.speed(0)

def face(x,y):                      #描绘一个笑脸的圆形轮廓，x, y 是圆心的坐标
    t.seth(0)                       
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("orange")
    t.circle(200)
    t.begin_fill()
    t.color("yellow")
    t.circle(200)
    t.end_fill()

def eye(a,b):                       #绘制一个眼睛，a, b 是眼睛的中心坐标
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


def eyeball1(c,d,l,p):              #c, d 是瞳孔的中心坐标，l 是半径，p 是绘制的角度
    t.seth(0)
    t.color("black")
    t.penup()
    t.goto(c,d)
    t.pendown()
    t.begin_fill()
    t.circle(l,p)
    t.end_fill()
    t.hideturtle()



def mouth(e,f,m,n):                 #e, f 是弧线的起始位置，m 是半径，n 表示绘制的角度
    t.seth(0)
    t.color("brown")
    t.penup()
    t.goto(e,f)
    t.pendown()
    t.circle(m,n)


    
def jx(g,h,j,k):                    #g 为矩形的宽度，h 和 j 为矩形眼睛的起始坐标，k 为矩形的高度
    t.seth(0)
    t.penup()
    t.goto(h,j)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for i in range(2):
        t.forward(g)
        t.right(90)
        t.forward(k)
        t.right(90)
    t.end_fill()



def eyeball2(q,r,s,v):              #q, r 是坐标，s 是半径，v 是绘制的角度
    t.seth(-86)
  
    t.penup()
    t.goto(q,r)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(s,v)
    t.end_fill()
    t.hideturtle()



face(-200,-200)
eye(-300,30)
eye(-125,30)
eyeball1(-300,30,25,360)
eyeball1(-125,30,25,360)
mouth(-212,-125,100,60)
mouth(-211,-125,100,-60)
face(300,-200)
eye(200,30)
eye(375,30)
eyeball1(200,30,25,360)
eyeball1(375,30,25,360)
mouth(292,-90,-90,60)
mouth(292,-90,-90,-60)


face(-200,-600)
jx(100,-300,-300,50)
jx(100,-180, -300,50)
eyeball2(-280,-305,35,180)
eyeball2(-180,-305,35,180)

t.seth(0)
t.color("brown")
t.penup()
t.goto(-300,-450)
t.pendown()
t.forward(150)


face(300,-600)
jx(100,150,-300,50)
jx(100,300,-300,50)
eyeball2(160,-305,35,180)
eyeball2(320,-305,35,180)

mouth(270,-460,120,50)
mouth(270,-460,120,-50)


















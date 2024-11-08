import turtle as t     #用t代替turtle
import time             #导入时间库

t1=t.Turtle()           #创建画笔
t2=t.Turtle()

def qg():               #子函数定义旗杆
    t2.penup()
    t2.goto(-300,-1000)
    t2.pendown()
    t2.setheading(180)
    t2.begin_fill()
    t2.forward(7)
    t2.right(90)
    t2.forward(2100)
    t2.right(90)
    t2.forward(7)
    t2.right(90)
    t2.forward(2100)
    t2.end_fill()
def jm(x,y):            #画旗面
    t1.setheading(0)
    t1.speed(0)
    t1.penup()
    t1.goto(x,y)
    t1.pendown()
    t1.color("red")
    t1.begin_fill()
    for _ in range(2):      #循环两次
        t1.forward(450)
        t1.left(90)
        t1.forward(300)
        t1.left(90)
    t1.end_fill()

def star(x,y,size,h):       #定义子函数画星星
    t1.penup()
    t1.goto(x,288+y)
    t1.pendown()
    t1.setheading(h)
    t1.color("yellow")
    t1.begin_fill()
    for _ in range(5):       #循环五次
        t1.forward(size)
        t1.right(144)
    t1.end_fill()

def main(x,y):          #定义主函数，画国旗
    jm(x,y)

    star(-270,-50+y,120,0)
    star(-140,-30+y,35,40)
    star(-100,-50+y,35,20)
    star(-100,-90+y,35,0)
    star(-140,-130+y,35,45)
    t1.hideturtle()
i=0
while(i<=30):           # 当 i<=30 时，继续循环,i控制国旗的高度
    t1.clear()          #清除之前绘制的国旗
    time.sleep(0.1)     #屏闪
    t1.speed(0)         # 设置绘制速度为最快
    t2.speed(0)         # 设置绘制速度为最快
    t2.speed(0)
    t.tracer(0)
    qg()
    t.tracer(1)       
    t.tracer(0)
    main(-310+11,-300+i*15) #调用main函数，国旗在y轴的变化是i*15
    t.tracer(10,1)          #10是绘制步长,1表示刷新频率
    t1.hideturtle()
    i=i+1                   #i自增1，控制y轴上升


























        
    
    

                

    
    
    

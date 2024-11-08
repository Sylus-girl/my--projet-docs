#------载入库-----------------
import turtle as t
t1=t.Turtle()
t2=t.Turtle()
import time
#------数据驱动---------------
qiux=[-600,-540,570,-300,-400,-50,150,250,250+30*1,250+30*2,250+30*3,250+30*4,450,-30 ]
qiuy=[400,340,-160,-170,160,60,-40,40,80,100,20,140,-20,350,-150]
#------------开始绘制----------
def qt(a,b,c,d,e):
    t1.seth(0)
    t1.penup()
    t1.goto(a,b)
    t1.pendown()
    t1.begin_fill()
    t1.color(c)
    for i in range(2):
        t1.forward(d)
        t1.right(90)
        t1.forward(e)
        t1.right(90)
    t1.end_fill()
  

def qiu(m,f,g,h,j,k):
    t1.seth(m)
    t1.penup()
    t1.goto(f,g)
    t1.color(h)
    t1.pendown()
    t1.begin_fill()
    t1.circle(j,k)
    t1.end_fill()
    

def xian(f,g,h,n):
    t1.seth(0)
    t1.penup()
    t1.goto(f,g)
    t1.pencolor(h)
    t1.pendown()
    t1.right(90)
    t1.forward(n)
    t.hideturtle()
def hu(o,p,q,r,s):
    t1.seth(180)
    t1.penup()
    t1.goto(o,p)
    t1.color(q)
    t1.pendown()
    t1.circle(r,s)
    t1.end_fill()
    


def yuanbai(m,f,g,h,j,k):
    t2.seth(m)
    t2.penup()
    t2.goto(f,g)
    t2.pendown()
    t2.begin_fill()
    t2.color(h)
    t2.circle(j,k)
    t2.end_fill()

t1.speed(0)
t2.speed(0)
t1.hideturtle()
t2.hideturtle()



qt(-600,400,"red",1200,600)
qt(-550,350,"green",1100,500)


qiu(45,qiux[0],qiuy[0],"#A8A8A8",-30,360)
qt(-600,360,"red",25,420)
qt(-560,400,"red",420,25)    
qiu(45,qiux[1],qiuy[1],"grey",20,360)


qiu(45,qiux[0],qiuy[2],"#A8A8A8",-30,360)
qt(-600,260,"red",25,420)
qt(-560,-175,"red",420,25)    
qiu(45,qiux[1],qiuy[3],"grey",20,360)

    
qiu(45,qiux[2],qiuy[0],"#A8A8A8",-30,360)
qt(575,360,"red",25,420)
qt(145,400,"red",420,25)    
qiu(45,qiux[2],qiuy[1],"grey",20,360)

qiu(45,qiux[2],qiuy[2],"#A8A8A8",-30,360)
qt(575,260,"red",25,420)
qt(145,-175,"red",420,25)    
qiu(45,qiux[2],qiuy[3],"grey",20,360)

xian(-300,350,"black",500)
hu(-300,175,"black",100,180)

qiu(0,qiux[3],qiuy[4],"#009240",20,360)
qiu(0,qiux[3],qiuy[5],"#E48B58",20,360)
qiu(0,qiux[3],qiuy[6],"yellow",20,360)
qiu(0,qiux[4],qiuy[5],"white",20,360)
qiu(0,qiux[5],qiuy[5],"#5BC4D1",20,360)
qiu(0,qiux[6],qiuy[5],"#E97979",20,360)

qiu(0,qiux[7],qiuy[5],"red",20,360)
qiu(0,qiux[8],qiuy[7],"red",20,360)
qiu(0,qiux[8],qiuy[8],"red",20,360)

qiu(0,qiux[9],qiuy[5],"red",20,360)
qiu(0,qiux[9],qiuy[9],"red",20,360)
qiu(0,qiux[9],20,"red",20,360)

qiu(0,qiux[10],qiuy[8],"red",20,360)
qiu(0,qiux[10],120,"red",20,360)
qiu(0,qiux[10],0,"red",20,360)
qiu(0,qiux[10],qiuy[7],"red",20,360)

qiu(0,qiux[11],qiuy[5],"red",20,360)
qiu(0,qiux[11],qiuy[9],"red",20,360)
qiu(0,qiux[11],qiuy[10],"red",20,360)
qiu(0,qiux[11],qiuy[11],"red",20,360)
qiu(0,qiux[11],qiuy[12],"red",20,360)

qiu(0,qiux[12],qiuy[5],"#2E1D21",20,360)


qiu(90,qiux[13],qiuy[13],"grey",30,180)

qiu(90,qiux[13],qiuy[14],"grey",30,-180)




p=1    # 定义一个标志以控制循环
i=0    # 初始化 i 为 0
while(p==1):     # 当 p 等于 1 时执行循环
    t2.clear()    # 清除t2 绘制的内容
    t.tracer(0)    # 暂停自动更新         # 持续绘制白球   
    yuanbai(0,300-(5-0.005*i)*i,-60+(3-0.005*i)*i,"#ffffff",10,360)
    t.tracer(5,1)    # 恢复自动更新
    time.sleep(0.02)  #暂停 0.02 秒
    i+=1           # 每次循环增加 i
    if(i==150):    #当 i 等于 150 时，循环已经运行了 150 次
        p=0          
 
















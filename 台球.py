#------载入库-----------------
import turtle as t
t.speed(0)
#------数据驱动---------------
qiux=[-600,-540,570,-300,-400,-50,150,250,250+30*1,250+30*2,250+30*3,250+30*4,450,-30 ]
qiuy=[400,340,-160,-170,160,60,-40,40,80,100,20,140,-20,350,-150]
#------------开始绘制----------
def qt(a,b,c,d,e):          #a、b 是矩形的左上角坐标，c 是填充颜色，d 是矩形的宽度，e 是矩形的高度
    t.seth(0)
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.begin_fill()
    t.color(c)
    for i in range(2):
        t.forward(d)
        t.right(90)
        t.forward(e)
        t.right(90)
    t.end_fill()
    t.hideturtle()

def qiu(m,f,g,h,j,k):    # m 是绘制方向，f、g 是圆心坐标，h 是颜色，j 是半径，k 是弧度
    t.seth(m)
    t.penup()
    t.goto(f,g)
    t.color(h)
    t.pendown()
    t.begin_fill()
    t.circle(j,k)
    t.end_fill()
    t.hideturtle()

def xian(f,g,h,n):       #绘制球台线。f、g 是起点坐标，h 是线条颜色，n 是线条长度
    t.seth(0)
    t.penup()
    t.goto(f,g)
    t.pencolor(h)
    t.pendown()
    t.right(90)
    t.forward(n)
    t.hideturtle() 
def hu(o,p,q,r,s):         #o、p 是圆心坐标，q 是颜色，r 是半径，s 是角度
    t.seth(180)
    t.penup()
    t.goto(o,p)
    t.color(q)
    t.pendown()
    t.circle(r,s)
    t.end_fill()
    t.hideturtle()







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












    

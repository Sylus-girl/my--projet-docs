import turtle as t
t.speed(0)
def jx(x,y):
    t.penup()
    t.color("red")
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(700)
        t.right(90)
        t.forward(520)
        t.right(90)
    t.end_fill()
      


def jxmin(d,e):
    t.penup()
    t.color("blue")
    t.goto(d,e)
    t.pendown()
    t.begin_fill()
    for j in range(2):
        t.forward(350)
        t.right(90)
        t.forward(250)
        t.right(90)
    t.end_fill()

def tw(f,g,h,k):
    t.penup()
    t.color("white")
    t.goto(f,g)
    t.pendown()
    t.begin_fill()
    for j in range(2):
        t.forward(h)
        t.right(90)
        t.forward(k)
        t.right(90)
    t.end_fill()

def xing(a,b):
    t.penup()
    t.color("white")
    t.goto(a,b)
    t.pendown()
    t.seth(0)
    t.begin_fill()
    for m in range(4):
        t.forward(20)
        t.right(144)
    t.end_fill()
    t.hideturtle()
    
            
     
        
jx(-300,400)
jxmin(-300,400)
tw(50,370,350,35)
tw(50,300,350,35)
tw(50,230,350,35)
tw(-300,160,700,35)
tw(-300,90,700,35)
tw(-300,20,700,35)
tw(-300,-50,700,35)

xing(-290,380)
xing(-230,380)
xing(-170,380)
xing(-110,380)
xing(-50,380)
xing(10,380)

xing(-260,360)
xing(-200,360)
xing(-140,360)
xing(-80,360)
xing(-20,360)

xing(-290,340)
xing(-230,340)
xing(-170,340)
xing(-110,340)
xing(-50,340)
xing(10,340)

xing(-260,320)
xing(-200,320)
xing(-140,320)
xing(-80,320)
xing(-20,320)

xing(-290,300)
xing(-230,300)
xing(-170,300)
xing(-110,300)
xing(-50,300)
xing(10,300)

xing(-260,280)
xing(-200,280)
xing(-140,280)
xing(-80,280)
xing(-20,280)

xing(-290,260)
xing(-230,260)
xing(-170,260)
xing(-110,260)
xing(-50,260)
xing(10,260)

xing(-260,230)
xing(-200,230)
xing(-140,230)
xing(-80,230)
xing(-20,230)

xing(-290,210)
xing(-230,210)
xing(-170,210)
xing(-110,210)
xing(-50,210)
xing(10,210)






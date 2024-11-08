import turtle as t
t.speed(0)
t.pensize(13)

def circle1(x,y,z,m,r):
    t.seth(r)
    t.penup()
    t.goto(x,y)
    t.color("blue")
    t.pendown()
    t.circle(z,m)
    t.hideturtle()
   

def circle2(a,b,l,n,s):
    t.seth(s)
    t.penup()
    t.goto(a,b)
    t.color("black")
    t.pendown()
    t.circle(l,n)    


def circle3(c,d,i,o,u):
    t.seth(u)
    t.penup()
    t.goto(c,d)
    t.color("red")
    t.pendown()
    t.circle(i,o)
    t.hideturtle()


def circle4(e,f,j,p,v):
    t.seth(v)
    t.penup()
    t.goto(e,f)
    t.color("yellow")
    t.pendown()
    t.circle(j,p)
    t.hideturtle()

def circle5(g,h,k,q,w):
    t.seth(w)
    t.penup()
    t.goto(g,h)
    t.color("green")
    t.pendown()
    t.circle(k,q)
    t.hideturtle()

circle1(-210,-50,100,360,0)
circle2(0,-50,100,360,0)
circle3(210,-50,100,360,0)
circle4(-110,-150,100,360,0)
circle5(105,-150,100,360,0)
circle1(-110,42,100,5,90)
circle2(100,42,100,5,90)
circle2(-5,-50,100,5,180)
circle3(210,-50,100,5,180)


    

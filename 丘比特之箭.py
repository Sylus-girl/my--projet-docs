import turtle as t
t.speed(0)
t.hideturtle()
t.tracer(0) 

def jian(x, y):
    t.seth(0)
    t.color("red")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(100)
        t.left(90)
        t.forward(20)
        t.left(90)
    t.end_fill()

def jiantou(x, y):  
    t.penup()
    t.goto(x + 100, y - 10)
    t.pendown()
    t.begin_fill()
    t.seth(270)
    t.left(135)
    t.forward(28)
    t.left(90)
    t.forward(28)
    t.end_fill()

def draw_arrow(x, y):
    jian(x, y)
    jiantou(x, y)

def move_arrow(step=0):
    t.clear()  
    draw_arrow(-200 + step * 7, -100)
    t.update()  

    if step < 30: 
        t.ontimer(lambda: move_arrow(step + 1), 100) 
move_arrow()
t.done()





import turtle
turtle.speed(2000)
def jump(penX):
    penX.setheading(0)            
    penX.forward(70)
    penX.setheading(-70)
    penX.forward(60)
    penX.setheading(80)
    penX.forward(70)
    penX.setheading(-75)
    penX.forward(132)
    penX.setheading(75)
    penX.forward(165)
    penX.setheading(-75)
    penX.forward(120)
    penX.setheading(65)
    penX.forward(72)
    penX.setheading(0)
    penX.forward(100)
    penX.setheading(0)
    
    
pen1=turtle.Turtle()
pen2=turtle.Turtle()
pen3=turtle.Turtle()
pen1.hideturtle()
pen2.hideturtle()
pen3.hideturtle()
pen1.color("red")
pen2.color("white")
pen3.color("blue")
pen1.pensize(8)
pen2.pensize(10)
pen1.pensize(10)

pen3.penup()
pen3.goto(-120,200)
pen3.write("心动的感觉",font=("Tempus Sans ITC",50,'normal'))

while(1):
    jump(pen1)
    jump(pen2)
    pen1.penup()
    pen1.goto(-350,1)
    pen1.pendown()
    pen2.penup()
    pen2.goto(-350,1)
    pen2.pendown()
    

    jump(pen1)
    jump(pen2)
    pen1.penup()
    pen1.goto(0,0)
    pen1.pendown()
    pen2.penup()
    pen2.goto(0,0)
    pen2.pendown()
   


    
    

import turtle as t

t.speed(0)

def  jx(x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("red")
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(550)
        t.right(90)
    t.hideturtle()




def write_text(text, position, font=("宋体", 45, "normal")):       # 移动画笔、写入文本、设置字体，字体大小，字体样式
    t.penup()
    t.goto(position)
    t.color("red")
    t.pendown()
    t.write(text, align="left", font=font)




def lx1(g,h,l):
    t.seth(0)
    t.penup()
    t.goto(g,h)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.right(120)
    for _ in range(2):
        t.forward(l)
        t.circle(1,60)
                          # 绘制直线部分
       
    for _ in range(2):
        t.circle(1,60)  # 注意这里半径是负数，表示圆弧方向相反
        t.forward(l)
    t.end_fill()
    
    # 隐藏画笔
    t.hideturtle()

jx(-200,300)
write_text("7",(-180,220))
write_text("7",(150,-230))
lx1(-166,220,20)
lx1(-100,220,60)
lx1(-100,80,60)
lx1(-100,-60,60)
lx1(100,220,60)
lx1(100,80,60)
lx1(100,-60,60)
lx1(100,-60,60)
lx1(0,150,60)
lx1(160,-130,20)






    



    
 

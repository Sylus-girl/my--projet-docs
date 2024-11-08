import turtle 
pen = turtle.Turtle()
pen.speed(0)
turtle.hideturtle()


def card():
    pen.color("blue")           # 设置画笔颜色
    pen.fillcolor("orange")    # 设置填充颜色
    pen.penup()
    pen.goto(20,0)
    pen.pendown()
    pen.begin_fill()
    for _ in range(2):
        pen.forward(500)  
        pen.right(90)
        pen.forward(300)
        pen.right(90)
       
    pen.end_fill()

card()                          # 调用函数绘制
turtle.hideturtle()


def write_text(text, position, font=("华文彩云", 30, "normal")):       # 移动画笔、写入文本、设置字体，字体大小，字体样式
    pen.penup()
    pen.goto(position)
    pen.pendown()
    pen.write(text, align="left", font=font)

# 调用函数添加文本
write_text("2024届编程实验室", (30, -50), font=("华文彩云",35, "bold"))
write_text("张慧民", (150, -130),font=("新宋体",40, "bold"))
write_text("特点：吃饭睡觉看帅哥", (50, -230),font=("华文彩云",25, "bold"))
write_text("地址：长江大学西校区", (150, -280),font=("华文彩云",20, "bold"))
write_text("QQ：1152363756", (50, -180),font=("华文彩云",25, "bold"))

pen.hideturtle()






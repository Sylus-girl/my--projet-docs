import turtle as t      #全局变量t作为turtle模块的别名
t.speed(10)
x0=0
y0=0

#---------------画旗面-------
def flag(x0,y0):          #定义 子函数flag 模块
    t.setheading(0)       #设置画笔朝向      
    t.penup()
    t.goto(x0,y0)
    t.pendown()
    t.begin_fill()
    t.color("red","red")
    t.forward(300)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(200)
    t.end_fill()

#----------画小星星-------------
def star(z,x,y,L):          #定义  子函数star 模块
    t.penup()               #z画笔方向,即星星初始角度，x,y起点坐标，L边长
    t.goto(x,y)                       
    t.pendown()             
    t.setheading(z)
    t.begin_fill()
    t.color("yellow","yellow")
    t.forward(L)
    t.right(144)
    t.forward(L)
    t.right(144)
    t.forward(L)
    t.right(144)
    t.forward(L)
    t.right(144)
    t.end_fill()
    
    
#------------------------主函数---------------------------------------
def china_flag(x0,y0,z1,x1,y1,z2,x2,y2,z3,x3,y3,z4,x4,y4,z5,x5,y5):
    flag(x0,y0)           #定义china_flag函数   绘制一个完整的国旗图案
    star(z1,x1,y1,60)      
    star(z2,x2,y2,20)     #x0和y0指定了国旗矩形背景的左上角坐标
    star(z3,x3,y3,20)
    star(z4,x4,y4,20)
    star(z5,x5,y5,20)
t.hideturtle()
   
 

#--------------------调用四次主函数  绘制四个国旗-----------------------------
china_flag(-200,-200,0,-180,-40,56,-100,-25,38,-80,-45,6,-80,-70,56,-100,-96)

china_flag(200,-200,0,220,-40,56,300,-25,38,320,-45,6,320,-70,56,300,-96)

china_flag(200,200,0,220,360,56,300,375,38,320,355,6,320,330,56,300,304)

china_flag(-200,200,0,-180,360,56,-100,375,38,-80,355,6,-80,330,56,-100,304)




















    
    
    
        

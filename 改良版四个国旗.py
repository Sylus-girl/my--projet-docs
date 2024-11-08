import turtle as t            #全局变量t作为turtle模块的别名
t.speed(10)

date1=[-200,-200]
date2=[200,-200]
#---------------画旗面-------
def flag(x,y):             #定义 子函数flag 模块         
    t.setheading(0)          #设置画笔朝向    
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("red","red")
    for i in range(2):
        t.forward(300)
        t.left(90)
        t.forward(200)
        t.left(90)
    t.end_fill()

#----------画小星星-------------

def star(z,x,y,L):                  #定义  子函数star 模块
    t.penup()                       #z画笔方向,即星星初始角度，x,y起点坐标，L边长
    t.goto(x,y)
    t.pendown()
    t.setheading(z)
    t.begin_fill()
    t.color("yellow","yellow")
    for i in range(4):
        t.forward(L)
        t.right(144)
    t.end_fill()
    
    
#------------------------主函数---------------------------------------
def china_flag(x,y):
    flag(x,y)
    star(0,x+20,y+160,60)       #定义china_flag函数   绘制一个完整的国旗图案
    star(56,x+100,y+175,20)
    star(38,x+120,y+155,20)       #x和y指定了国旗矩形背景的左上角坐标
    star(6,x+120,y+130,20)
    star(56,x+100,y+104,20)
t.hideturtle()
   
 

#--------------------------------绘制两面国旗--------------------------------
china_flag(date1[0],date1[1])
china_flag(date2[0],date2[1])

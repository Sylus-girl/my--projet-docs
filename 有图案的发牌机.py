import random as r  #导入 random 模块并重命名为 r，用于生成随机数
import turtle as t
t.speed(5)
pk=["\u2665A","\u26652","\u26653","\u26654","\u26655","\u26656","\u26657","\u26658", "\u26659","\u266510","\u2665J","\u2665Q","\u2665K"
    ,"\u2660A","\u26602","\u26603", "\u26604","\u26605","\u26606","\u26607","\u26608", "\u26609","\u266010","\u2660J", "\u2660Q","\u2660K"
    ,"\u2666A","\u26662","\u26663","\u26664","\u26665","\u26666","\u26667","\u26668", "\u26669","\u266610","\u2666J","\u2666Q","\u2666K",
    "\u2663A","\u26632","\u26633","\u26634","\u26635","\u26636","\u26637","\u26638", "\u26639","\u266310","\u2663J","\u2663Q","\u2663K","blackJOKER"
    ,"redJOKER"]
                        #定义一副扑克牌 pk 列表，包括黑桃（♠）、红桃（♥）、方块（♦）、梅花（♣）的 A-K 牌，以及黑红大小王。

#\u2660 ♠ ：黑桃
#\u2666 ♦ ：方块
#\u2663 ♣ ：梅花


dizhu=[]        #定义三个空列表
nm1=[]
nm2=[]
def jx(x1,y1):   #jx 用于在指定坐标位置绘制一个长方形牌的框
    t.seth(0)
    t.penup()
    t.goto(x1+a*25,y1)
    t.pendown()
    for i in range(2):
        t.forward(40)
        t.right(90)
        t.forward(60)
        t.right(90)
    t.penup()
    t.goto(500,1000)    #将画笔移出视图，避免影响其他图形的绘制。
    t.pendown()   



def num(x1,y1,b1,c1):   # num用于在指定位置书写文字b1 
                        #c1 是字体大小,是要显示的内容
    t.seth(0)
    t.penup()
    t.goto(x1+a*25,y1)
    t.pendown()
    t.write(b1,font=("微软雅黑",c1,"normal"))   
    t.penup()
    t.goto(500,1000)
    t.pendown() 
    

def wang(x1,y1,b1,c1,d1):   # wang 用于书写黑/红王的文字内容
    t.seth(0)               # d1指定颜色
    t.penup()
    t.goto(x1+a*25,y1)
    t.pendown()
    t.color(d1)
    t.write(b1,font=("微软雅黑",c1,"normal"))   
    t.penup()
    t.goto(500,1000)
    t.pendown() 
    t.color("black")


def jx1(x2,y2,b2,color1,color2):  #jx1 绘制具有圆角的卡片长方形框，并填充颜色
    t.penup()                     #color1 为边框颜色，color2 为填充颜色
    t.goto(x2+25*a,y2)
    t.color(color1,color2)
    t.pendown()
    t.begin_fill()
    for m in range(2):
        t.forward(b2*0.8)
        t.circle(b2*0.1,90)
        t.forward(b2*1.3)
        t.circle(b2*0.1,90)
    t.end_fill()
    t.penup()
    t.goto(500,1000)
    t.pendown()
        
t.color("")             #初始化画笔颜色为空
t.tracer(False)     #t.tracer(False) 关闭 turtle 自动更新屏幕
for a in range(20):
    t.color("black")
    b=r.randint(0,len(pk)-1)             # 随机抽取一张牌，将其绘制成地主的牌，
    dizhu.append(pk[b])                  #并从 pk 中移除
    jx1(-185,170,40,"black","white")
    if(pk[b][0]=="\u2665"):
        t.color("red")
    elif(pk[b][0]=="\u2666"):
        t.color("red")
    elif(pk[b][0]=="\u2660"):
        t.color("black")
    elif(pk[b][0]=="\u2663"):
        t.color("black")

    if(pk[b]=="blackJOKER"):
        wang(-178,210,pk[b][5],8,"black")
        wang(-180,200,pk[b][6],8,"black")
        wang(-180,210,pk[b][7],8,"black")
        wang(-180,210,pk[b][8],8,"black")
        wang(-180,210,pk[b][9],8,"black")

    elif(pk[b]=="redJOKER"):
        wang(-178,210,pk[b][3],8,"red")
        wang(-180,200,pk[b][4],8,"red")
        wang(-180,190,pk[b][5],8,"red")
        wang(-180,180,pk[b][6],8,"red")
        wang(-180,170,pk[b][7],8,"red")
    elif(a==19):
        num(-184,170,pk[b][0],25)  #对于普通牌，num显示牌面
        num(-183,210,pk[b][-1],11)
        num(-184,200,pk[b][0],11)
        t.color("black")
        num(-174,210,"地主",8,)#标出地主牌



    else:
        if(pk[b][-1]=="0"):
            num(-180,212,"10",9)
            num(-180,200,pk[b][0],11)
        if(pk[b][-1]!="0"):
            num(-180,210,pk[b][-1],11)
            num(-180,200,pk[b][0],11)
    del pk[b]

    
            
for a in range(16):
    t.color("black")      # 循环随机抽取16张牌
    c=r.randint(0,len(pk)-1)
    nm1.append(pk[c])           #分别放入 nm1 和 nm2 列表中，并绘制成农民的牌
    jx1(-185,-30,40,"black","white")
    if(pk[c][0]=="\u2665"):     #用 jx1 绘制空白卡片，并用 num 或 wang 显示牌面。
        t.color("red")
    elif(pk[c][0]=="\u2666"):
        t.color("red")
    elif(pk[c][0]=="\u2660"):
        t.color("black")
    elif(pk[c][0]=="\u2663"):
        t.color("black")

    if(pk[c]=="blackJOKER"):
        wang(-178,10,pk[c][5],8,"black")
        wang(-180,0,pk[c][6],8,"black")
        wang(-180,-10,pk[c][7],8,"black")
        wang(-180,-20,pk[c][8],8,"black")
        wang(-180,-30,pk[c][9],8,"black")

    elif(pk[c]=="redJOKER"):
        wang(-178,10,pk[c][3],8,"red")
        wang(-180,0,pk[c][4],8,"red")
        wang(-180,-10,pk[c][5],8,"red")
        wang(-180,-20,pk[c][6],8,"red")
        wang(-180,-30,pk[c][7],8,"red")

    elif(a==16):
        num(-171,170,pk[b][0],25)
        num(-180,210,pk[b][-1],11)
        num(-180,200,pk[b][0],11)
       


    else:
        if(pk[c][-1]=="0"):
            num(-180,12,"10",11)
            num(-180,0,pk[c][0],11)
        if(pk[c][-1]!="0"):
            num(-180,10,pk[c][-1],11)
            num(-180,0,pk[c][0],11)

    del pk[c]


for a in range(16):
    t.color("black")
    d=r.randint(0,len(pk)-1)
    nm2.append(pk[d])
    jx1(-185,-230,40,"black","white") 
    if(pk[d][0]=="\u2665"):
        t.color("red")
    elif(pk[d][0]=="\u2666"):
        t.color("red")
    elif(pk[d][0]=="\u2660"):
        t.color("black")
    elif(pk[d][0]=="\u2663"):
        t.color("black")
    
    if(pk[d]=="blackJOKER"):
        wang(-178,-190,pk[d][5],8,"black")
        wang(-180,-200,pk[d][6],8,"black")
        wang(-180,-210,pk[d][7],8,"black")
        wang(-180,-220,pk[d][8],8,"black")
        wang(-180,-230,pk[d][9],8,"black")

    elif(pk[d]=="redJOKER"):
        wang(-178,-190,pk[d][3],8,"red")
        wang(-180,-200,pk[d][4],8,"red")
        wang(-180,-210,pk[d][5],8,"red")
        wang(-180,-220,pk[d][6],8,"red")
        wang(-180,-230,pk[d][7],8,"red")

     #最后一张牌画出图案
    elif(a==16):
        num(-169,-230,pk[b][0],25)
        num(-178,-190,pk[b][-1],11)
        num(-179,-200,pk[b][0],11)
        

    else:
        if(pk[d][-1]=="0"):
            num(-180,-188,"10",9)
            num(-180,-200,pk[d][0],11)
        if(pk[d][-1]!="0"):
            num(-180,-190,pk[d][-1],11)
            num(-180,-200,pk[d][0],11)

    
    del pk[d]






















    

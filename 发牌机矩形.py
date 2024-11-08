import random as r      # 引入 random 模块用于生成随机数，并重命名为 r
import turtle as t
t.speed(0)
pk=["红心A","红心2","红心3","红心4","红心5","红心6","红心7","红心8", "红心9","红心10","红心J","红心Q","红心K"
    ,"黑桃A","黑桃2","黑桃3", "黑桃4","黑桃5","黑桃6","黑桃7","黑桃8", "黑桃9","黑桃10","黑桃J", "黑桃Q","黑桃K"
    ,"方块A","方块2","方块3","方块4","方块5","方块6","方块7","方块8", "方块9","方块10","方块J","方块Q","方块K",
    "梅花A","梅花2","梅花3","梅花4","梅花5","梅花6","梅花7","梅花8", "梅花9","梅花10","梅花J","梅花Q","梅花K","小王"
    ,"大王"]

dizhu=[]
nm1=[]
nm2=[]

def jx(x,y,a):      #jx 函数用来绘制扑克牌的矩形边框
    t.seth(0)
    t.penup()
    t.goto(x+a*45,y)  #x、y 表示初始位置，a 控制每张牌在水平方向的偏移量，以实现横向排列
    t.pendown()
    for i in range(2):
        t.forward(40)
        t.right(90)
        t.forward(60)
        t.right(90)
    

def num(x,y,a,b):
    t.seth(0)
    t.penup()
    t.goto(x+a*45.1,y)    # 移动到目标位置
    t.pendown()
    t.write(b,font=("Arial",10,"normal"))   # 在位置 b 写上牌面内容
    
t.color("black")
t.tracer(0)   # 关闭自动屏幕刷新

for a in range(20):
    c=r.randint(0,len(pk)-1)  # 随机选择一张牌
    dizhu.append(pk[c])  # 将选择的牌添加到地主的牌列表
    jx(-480,200,a)        # 调用 jx 函数绘制边框
    num(-480,160,a,pk[c])   # 调用 num 函数显示牌面内容
    del pk[c]        # 从总牌列表中移除该牌


for a in range(17):
    d=r.randint(0,len(pk)-1)
    nm1.append(pk[d])     # 添加到农民1的牌列表
    jx(-400,100,a)
    num(-400,60,a,pk[d])
    del pk[d]


for a in range(17):
    e=r.randint(0,len(pk)-1)
    nm2.append(pk[e])   # 添加到农民2的牌列表
    jx(-400,0,a)
    num(-400,-40,a,pk[e])
    del pk[e]

t.penup()
t.goto(-470, 200)
t.write("地主", font=("微软雅黑", 12, "normal"))

t.penup()
t.goto(-400, 100)
t.write("农民1", font=("微软雅黑", 12, "normal"))

t.penup()
t.goto(-400, 0)
t.write("农民2", font=("微软雅黑", 12, "normal"))
t.hideturtle()
t.update()

#write 标记“地主”、“农民1”、“农民2”。


    

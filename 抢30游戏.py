start=int(input("输入游戏初始值："))
add=int(input("输入每次比拼最多能累加的数值："))
now=start
print("当前值为：",now)
while (1):     #外层表示游戏将持续进行，直到玩家中的某一方胜出为止
    while(1):      #表示玩家一的输入步骤，将一直要求输入直到输入合法为止。
        a=int(input("请玩家一输入不超过{}累加的数值：".format(add)))
        if  a<=add:            #如果输入合法，则跳出循环
            break
        print("请重新输入不超过{}的数值：".format(add))   #如果输入不合法，给出提示并重新请求输入
         
    now+=a
    print("现在的数值为：",now)
    if now==30:
            print("玩家一胜利！")    #累加后的 now 恰好等于 30，则玩家一胜利，并终止整个游戏循环
            break

    while(1):
        b=int(input("请玩家二输入不超过{}累加的数值：".format(add)))
        if b<=add:
            break
        print=("请重新输入不超过{}的数值：")
         
    now+=b
    print("现在的数值变成了：",now)   
    if now==30:
            print("玩家二胜利！")
            break

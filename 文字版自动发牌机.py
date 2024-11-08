import random as r       #使用 random 模块的别名 r，用于随机选择牌。

pk=['红心A','红心2','红心3','红心4','红心5','红心6','红心7','红心8', '红心9','红心10','红心J','红心Q',
    '红心K','黑桃A','黑桃2','黑桃3', '黑桃4','黑桃5','黑桃6','黑桃7','黑桃8', '黑桃9','黑桃10','黑桃J',
    '黑桃Q','黑桃K','方块A','方块2','方块3','方块4','方块5','方块6','方块7','方块8', '方块9','方块10','方块J',
    '方块Q','方块K','梅花A','梅花2','梅花3','梅花4','梅花5','梅花6','梅花7','梅花8', '梅花9','梅花10','梅花J',
    '梅花Q','梅花K','小王','大王']

dizhu=[]         #dizhu 用于存储地主的手牌。
                  #nm1 和 nm2 用于存储两个农民的手牌。
nm1=[]
nm2=[]
for i in range(17):      #表示循环 17 次，每次给每个玩家发 1 张牌。
    num1=r.randint(0,len(pk)-1)    #从 pk 中随机抽一张牌        
    dizhu.append(pk[num1])           #将这张牌添加到对应的玩家手牌列表
    del pk[num1]                #从牌堆 pk 中移除该牌，避免重复抽取。
    num2=r.randint(0,len(pk)-1)
    nm1.append(pk[num2])
    del pk[num2]
    num3=r.randint(0,len(pk)-1)
    nm2.append(pk[num3])
    del pk[num3]
            
        
print(nm1)
print("\n\n")

print(nm2)
print("\n\n")

dizhu.append(pk)
print(dizhu)

print("欢迎来到无尽密室")
sex=input("请选择你的性别？1-男 2-女")
if(sex=="1"):
    print("欢迎你，侠士!")
else:
    print("欢迎你，神女！")
name=input("请问玩家，你的名字是？")
print("欢迎你,",name,"你的名字听起来很不错！")
age=input("你多大了？")
if(int(age)<=20):
    print("少年英雄,纵世奇才！")
else:
    print("江湖老手，身经百战！")
job=input("请选择你的职业？1-法师 2-战士 3-刺客")
if(job=="1"):
    print("你选择了法师，这个职业技能丰富！")
elif(job=="2"):
    print("你选择了战士，这个职业生存能力强！")
elif(job=="3"):
    print("你选择了刺客，这个职业身手敏捷！")
partner=input("请选择你的伙伴，1-吴邪   2-王月半  3-张起灵")
if(partner=="1"):
    print("恭喜你喜提高材生一枚!")
elif(partner=="2"):
    print("恭喜你喜提爆破小王子一枚！")
elif(partner=="3"):
    print("恭喜你喜提武力值第一的帅哥一枚！")
#------------------------------------欢迎词--------------------------------
print("\n\n===============================================================")
print(name,",欢迎你来到无尽密室",end=",")
if(int(age)<=20):
    print("考虑到你是新手，建议你选择简单模式。")
else:
    print("考虑到你是老手，建议你选择困难模式。")

    
    
    
     

          

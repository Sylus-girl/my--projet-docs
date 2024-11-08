def calculate_gpa():
    # 输入学分和成绩
    x1=float(input("形势与政策学分："))
    y1=int(input("形势与政策成绩为："))
    x2=float(input("中国近代史纲要学分："))
    y2=int(input("中国近代史纲要成绩为:"))
    x3=float(input("大学英语听说（上）学分："))
    y3=int(input("大学英语听说（上）成绩为："))
    x4=float(input("计算机概论学分："))
    y4=int(input("计算机概论成绩为："))
    x5=float(input("体育（1）学分："))
    y5=int(input("体育（1）成绩为:"))
    x6=float(input("军事理论学分："))
    y6=int(input("军事理论成绩为："))
    x7=float(input("高等数学B（上）学分："))
    y7=int(input("高等数学B（上）成绩为："))
    x8=float(input("大学英语（上）学分："))
    y8=int(input("大学英语（上）成绩："))
           
    #计算绩点差值和加权分数            
    z1=(y1-50)/10
    z2=(y2-50)/10
    z3=(y3-50)/10
    z4=(y4-50)/10
    z5=(y5-50)/10
    z6=(y6-50)/10
    z7=(y7-50)/10
    z8=(y8-50)/10
            
    m1=x1*z1
    m2=x2*z2
    m3=x3*z3
    m4=x4*z4
    m5=x5*z5
    m6=x6*z6
    m7=x7*z7
    m8=x8*z8

    # 计算总加权分数和总学分
    h1=m1+m2+m3+m4+m5+m6+m7+m8
    h2=x1+x2+x3+x4+x5+x6+x7+x8
    # 计算加权平均绩点
    h3=h1/h2
    
    
    # 输出结果
    print("第一学期加权平均绩点：%.2f"%h3)

# 调用函数
name = input("请输入你的名字：")
print(f"你好，（name），以下是你的GPA计算结果：")
calculate_gpa()



an = "y"
while an == "y": 
    calculate_gpa()
    an = input("你想再测一次吗？（y/n）: ").lower()  # 确保输入为小写



 







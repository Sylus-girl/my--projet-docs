print("=================成绩录入===================")
k=input("姓名1:")
grade=input("成绩1:")
a=input("姓名2:")
b=input("成绩2:")
c=input("姓名3:")
d=input("成绩3:")
e=input("姓名4:")
f=input("成绩4:")
print("\n")
g=1
h=2
i=3
j=4
print("本小组的成绩录入如下：")
print("序号","姓名","成绩")
print("",g,"  ",k,  grade)
print("",h,"  ",a,  b)
print("",i,"  ",c,  d)
print("",j,"  ",e,  f)
grades={"k":grade,"a":b,"c":d,"e":f}
max_name=""
max_score=-1
for name,score in grades.items():
    if int(score)>int(max_score):
        max_score=score
        max_name=name
print(f"最高分是{max_score},获得者是{max_name}.")




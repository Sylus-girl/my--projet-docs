sum=0
for i in range(101):
    if i%3==0 or '3' in str (i):
        print("",i,end='')
        sum+=i
print('')
print("这些数之和为：",sum)


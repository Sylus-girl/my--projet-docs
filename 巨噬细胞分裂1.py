sum=26625
for i in range(10,-1,-1):
    sum=int((sum+1)/2)
    print("{}小时后有{}个细胞".format(i,sum))
print("最开始巨噬细胞有：{}".format(sum))

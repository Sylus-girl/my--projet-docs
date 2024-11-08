def sort(ss):               #这里的 ss 参数实际上在函数体内没有被使用
    print(ls)               # 打印原始列表
    for j in range(len(ls)-1):       # 外层循环，控制排序的轮数
        for i in range(len(ls)-j-1):    # 内层循环，进行当前轮次的比较和交换
            if ls[i] < ls[i+1]:         #降序排序
                ls[i], ls[i+1] = ls[i+1], ls[i]     # 交换元素
     
ls = [12,0,10,9,8,-1,21,-6]
sort(ls)
print(ls)            # 打印排序后的列表

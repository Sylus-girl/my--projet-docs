def sort(ss):
    for i in range(len(ss)):  # i 指向未排序部分的第一个元素
        key = i  # 假设当前 i 是最大值
        for j in range(i + 1, len(ss)):  # 找到未排序部分的最大值
            if ss[j]>ss[key]:
                key = j  # 更新最大值的位置

       
        ss[i], ss[key] = ss[key], ss[i]

ls = [12, 0, 78, 66, -2, 10, 9, 8, -1, 21, -6]
sort(ls)
print(ls)

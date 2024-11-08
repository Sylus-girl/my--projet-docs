while True:
    n = int(input("请输入年份："))
    a = []
    b = []
    sum = 0
    num = 0

    for i in range(2025, n):
        if i % 4 == 0 and i % 100 != 0:
            a.append(i)
            sum += 1
        elif i % 400 == 0:
            b.append(i)
            num += 1

    print("普通闰年有：")
    for i in range(0, len(a), 10):               #用 range() 函数生成从 0 到 len(a) 的索引序列,每次步进 10。
        print(", ".join(map(str, a[i:i + 10])))  # 每10个普通闰年一行输出

    print("世纪闰年有：")
    for i in range(0, len(b), 10):               # 使用 join() 方法将当前10个元素转换为以逗号分隔的字符串
        print(", ".join(map(str, b[i:i + 10])))  # 每10个世纪闰年一行输出

    # 询问用户是否继续
    choice = input("想再玩一次吗？输入 'y' 继续，输入 'n' 退出：")
    if choice.lower() != 'y':  # 如果输入不是 'y'，则退出循环
        print("游戏结束")
        break

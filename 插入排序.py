def sort(ss):           # 定义了sort函数
    print(ls)
    for i in range(1,len(ls)):      #对 ls 进行遍历，从第二个元素开始，认为第一个元素是已排序的
        key=ls[i]             # 将当前遍历到的元素赋值给变量 key，这个元素将是尝试插入到已排序序列中的元素
        j=i-1                # 初始化变量 j 为 i-1，即 key 元素的前一个元素的索引
        while j>=0 and ls[j]<key:
            ls[j+1]=ls[j]       #将 j 索引处的元素向后移动一位，为 key 元素腾出空间
            j-=1    # 将j减1，继续与前一个元素进行比较
        ls[j+1]=key   # 当找到 key 元素应该插入的位置时（即 j+1 的位置），将 key 插入到这个位置
ls = [12,0,10,9,8,-1,21,-6]
sort(ls)
print(ls)

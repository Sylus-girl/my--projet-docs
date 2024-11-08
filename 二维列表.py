ls1=[12,0,8,9,6,1,21,46]
ls2=[3,88,-2,90,100]
ls3=[6,-3,9,12,44,0,50,70,-23,8]
def sort(ss):
    print(ss)
    for i in range(1,len(ss)):        # 从第二个元素开始遍历，认为第一个元素是一个已排序的序列
        key=ss[i]    # 当前要插入的元素
        j=i-1       # 从前一个元素开始比较
        while j>=0 and ss[j]>key:    # 如果前一个元素比当前元素大，则将其向后移动  
            ss[j+1]=ss[j]       # 将较大的元素向后移动一位
            j-=1        # 继续与前一个元素比较
        ss[j+1]=key   # 找到正确的位置后，插入当前元素

sort(ls1)
sort(ls2)
sort(ls3)
print("")
print("")
print(ls1)
print(ls2)
print(ls3)
    
    

def xibao(num,sum):
    n=1
    y=0
    while y<sum:
            y =(num - 1)*(2**n)+1
            if y>=sum:
                return n
            n=n+1
result=xibao(27,100001)
print("最少需要的时间为：{}小时".format(result))

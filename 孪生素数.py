from math import sqrt
def prime(n):
    if n>1:
        for i in range(2,int(sqrt(n)+1)):
            if n%i==0:
                return 0
        return 1
    return 0

def twin_primes(a,b):
    twin_primes_list = []
    for i in range(a,b-1):
        if prime(i) and prime(i+2):
                twin_primes_list.append((i,i+2))
    return twin_primes_list
a=1000
b=2000
twin_primes2=twin_primes(a,b)

print("1000到2000之间的孪生素数有：",twin_primes2)
print("")
print("1000到2000的孪生素数一共有：",len(twin_primes2),"组")


#排列
def fact(n):
    s =1
    for i in range(1,n+1):
        s*=i
    return s


def A(n,m):
    s =1
    for i in range(n-m+1,n+1):
        s*=i
    return s


def A2(n,m):
    return fact(n)//fact(n-m)


#组合
def C(n,m):
    return A(n,m)//fact(m)



    
   

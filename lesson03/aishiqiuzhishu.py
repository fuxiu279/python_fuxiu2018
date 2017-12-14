#埃拉托色尼筛选法求质数，只适用于n小于100时

def aishizhishu(n):
    ls =[2,3,5,7]
    for i in range(2,n):
        if i%2 ==0 or i%3 ==0 or i%5 ==0 or i%7 ==0:
            continue
        ls.append(i)
    return ls

print(aishizhishu(100))
       

import math

# 埃拉托色尼筛法
def zhishu(max):
    li = []
    for i in range(2, max + 1):
        if i > 2 and i % 2 == 0:
            li.append(0)
        else:
            li.append(i)

    for i in range(3, int(math.sqrt(max)) + 1):
        if li[i - 2] != 0:
            for j in range(i + i, max + 1, i):
                li[j - 2] = 0

    outp=[]
    for i in li:
        if i != 0:
            outp.append(i)

    return outp


print(zhishu(100))

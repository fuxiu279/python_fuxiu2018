#埃拉托色尼筛选法求质数

def aishizhishu(n):
    ls =[2,3,5,7]
    for i in range(2,n):
        if i%2 ==0 or i%3 ==0 or i%5 ==0 or i%7 ==0:
            continue
        ls.append(i)
    return ls

print(aishizhishu(100))
       

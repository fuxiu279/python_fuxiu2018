

#100以内全部质数

print('输出100以内全部质数')
for i in range(2,101):
    shizhishu = True
    for j in range(2,i):
        if i%j == 0:
            shizhishu = False
            break
    if shizhishu == True:
          print(i)
      
       

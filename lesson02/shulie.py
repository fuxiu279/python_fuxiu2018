

#斐波那契数列前100项，并输出99项与100项的比值
print('输出斐波那契数列前100项，及99项与100项的比值')
a = 1
b = 1
i = 2
i99,i100 =1,1
print(1,a)
print(2,b)
while i<100:
    i +=1
    c = a+b
    a = b
    b = c
    print(i,c)
    if i == 99:
        i99 = c
    if i == 100:
        i100 = c
        print(i99/i100)



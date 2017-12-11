'''
#求1+2+3...100 = ?
s = 0
for i in range (1,101):
    s +=i
print(s)

#求2+4+6...100 = ?
s = 0
for i in range (1,101):
    if i%2 == 0:
      s +=i
print(s)


s = 0
for i in range (1,101):
    if i%2 != 0:continue
    s +=i
print(s)
'''

#打印0-100，满足偶数，各个数位相加9，eg:18,1+8=9
for i in range (1,100):
    if i%2 == 0 and i%10 +i//10 ==9:
        print(i)

for i in range (1,100):
    if i%2 != 0: continue
    if i%10 +i//10 ==9:
        print(i)

#输出偶数，各个数位相加为9，要7个
s,i = 0,0
while True:
    i+=1
    if i%2 == 1:continue
    cs,ci = 0,i
    while ci>0 :
        cs += ci%10
        ci //= 10
    if cs == 9:
         s += 1
         print(i)
         if s == 7:break
    
        


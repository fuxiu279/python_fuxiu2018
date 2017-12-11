#洗衣流程
print('请输入水位')
level = input()
'''
if xxx
elif
   do...
else
   do...

'''

if level=='h':
    print('注水50L')
    print('搅拌60min')
    print('放水')
elif level=='l':
    print('注水20L')
    print('搅拌30min')
    print('放水')


#甩干流程
print('请输入甩干次数')
times = int(input())
for i in range(times):
    print('注水30L')
    print('搅拌5min')
    print('放水')
    print('高速搅拌')


def wash(level):
    #洗衣流程
    if level=='high':
        print('注水50L')
        print('搅拌60min')
        
    elif level=='low':
        print('注水20L')
        print('搅拌30min')
        

def dry(times):
    #甩干流程
    print('放水且甩干')
    for i in range(times):
        print('注水30L')
        print('搅拌5min')
        print('甩干')
        
        
def wash_dry(obj,level='low',times=1):
    '''
    欢迎使用
    obj投入衣物
    level设定水位
    times甩干次数
    '''
    print('开始洗衣')
    wash(level)
    dry(times)
    print('%s 洗干净了'%obj)


wash_dry('衣服')
wash_dry('毛毯','high',5)
wash_dry('被套',times=2)


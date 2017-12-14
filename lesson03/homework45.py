#输出文件层级

import os
print('输出文件层级')
def  wenjiancengji1(dirname):
    nn = os.listdir(dirname)
    for i in  range (0,len(nn)):
        print(nn[i])
print(wenjiancengji1('C:\\Users\\a\\Desktop\\python\\python_fuxiu2018'))




#输出文件层级并输出子文件夹以及文件

import os
print('输出文件层级并输出子文件夹以及文件')
def  wenjiancengji(dirname):
    mm = os.listdir(dirname)
    for i in  range (0,len(mm)):
        path = os.path.join(dirname,mm[i])
        if os.path.isdir(path):
            print (mm[i],':')
            wenjiancengji(path)
        else:
            print ('--',mm[i])
print(wenjiancengji('C:\\Users\\a\\Desktop\\python\\python_fuxiu2018'))




import os

fp=open('D:\\Python3\\apps\\Temp\\' + 'forum.worldofwarships.username.txt','r')

i=1
lines = fp.readlines()#读取全部内容  
    
fp.close()

addr=";".join(lines)

f=open('D:\\Python3\\apps\\Temp\\' + 'addr.txt','w')
f.write(addr)
f.close()

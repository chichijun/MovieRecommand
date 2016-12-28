# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:31:43 2016

@author: Administrator
"""

import numpy as np
from matplotlib.pyplot import plot, show
import matplotlib.pyplot as plt
import pandas as pd
import os 

  

def GetFileList(dir, fileList): 
    newDir = dir 
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk')) 
    elif os.path.isdir(dir):   
        for s in os.listdir(dir): 
            #如果需要忽略某些文件夹，使用以下代码 
            #if s == "xxx": 
                #continue 
            newDir=os.path.join(dir,s) 
            GetFileList(newDir, fileList)   
    return fileList 




'''
x = np.linspace(0, 2 * np.pi, 30) #创建一个包含30个点的余弦波信号
e=np.linspace(0,9,30)
l=[0 for i in e]#只是一条基准线
wave = np.cos(x)
#print wave
plt.figure(1)
plt.subplot(111)
plt.plot(wave)
plt.plot(l)
plt.xticks([])
plt.xlabel(u"cos x from 0 to 2π")
show()
transformed = np.fft.fft(wave)  #使用fft函数对余弦波信号进行傅里叶变换。
#print np.all(np.abs(np.fft.ifft(transformed) - wave) < 10 ** -9)  #对变换后的结果应用ifft函数，应该可以近似地还原初始信号。
plot(transformed)  #使用Matplotlib绘制变换后的信号。
show()


f=open("E:\\DataMining\\synthetic_control\\synthetic_control_TRAIN")
#首先获取到一共有多少维度
reader=pd.DataFrame() 
reader= pd.read_table('E:\\DataMining\\synthetic_control\\synthetic_control_TRAIN',header=None,sep=',')#iterator=True,chunksize=1000)    
dim=reader.shape[1]-1
x=np.linspace(0,dim/10,dim)
trueReader=reader.iloc[:,1:]#去除第一列
print trueReader 
firstline=reader.iloc[0:1,:]
'''
#print firstline #是一个Series
#firstline.plot()
#print wave



#关于saveTxt的格式 http://www.programcreek.com/python/example/52629/numpy.savetxt

def FourierTransAndSaveTxt():
    list = GetFileList('E:\\DataMining\\Data_collection0', []) 
    for e in list:
        print e
        f=open(e)
        res=[]
        Mx=[]
        lis=[]
        for line in f:
            lis=line.strip().split(',')    
            cl=lis[0]
            lis=[float(i) for i in lis]    
            res.append([cl])
            Mx.append(lis[1:])   
        f.close()
            #print Mx
        dim=len(lis)-1    
        j=0    
        for i in Mx:
            waveone=np.array(i)
          #  print waveone.shape[1]
            x = np.linspace(0, 30, 30)
            plt.figure(1)
            plt.subplot(111)
            plt.plot(waveone)
            plt.show()
            Matrix=np.array(Mx)
            transWave=np.fft.fft(waveone)
            choseWave=transWave[0:21]   
            choseWave=[float(i) for i in choseWave]
            res[j]+=choseWave
            #print transWave
            plot(transWave)
            show()
            j+=1
      #  print res
        res=np.array(res)
       # np.savetxt(e+"_chosed",res,fmt='%s',newline='\n')


FourierTransAndSaveTxt()
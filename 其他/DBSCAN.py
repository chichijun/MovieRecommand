# -*- coding: utf-8 -*-
'''
Created on Tue Nov 15 18:39:11 2016

@author: Administrator
'''
from __future__ import division
from pandas import *
import pandas as pd
from sklearn import cluster
from sklearn import datasets
import datetime
from sklearn.cluster import DBSCAN

"""
 1 DBSCAN(D, eps, MinPts)
 2    C = 0                                          //类别标示
 3    for each unvisited point P in dataset D        //遍历
 4       mark P as visited                           //已经访问
 5       NeighborPts = regionQuery(P, eps)           //计算这个点的邻域    
 6       if sizeof(NeighborPts) < MinPts             //不能作为核心点
 7          mark P as NOISE                          //标记为噪音数据
 8       else                                        //作为核心点，根据该点创建一个类别
 9          C = next cluster
10          expandCluster(P, NeighborPts, C, eps, MinPts)    //根据该核心店扩展类别
11           
12 expandCluster(P, NeighborPts, C, eps, MinPts)
13    add P to cluster C                                     //扩展类别，核心店先加入
14    for each point P' in NeighborPts                       //然后针对核心店邻域内的点，如果该点没有被访问，
15       if P' is not visited
16          mark P' as visited                               //进行访问
17          NeighborPts' = regionQuery(P', eps)              //如果该点为核心点，则扩充该类别
18          if sizeof(NeighborPts') >= MinPts
19             NeighborPts = NeighborPts joined with NeighborPts'
20       if P' is not yet member of any cluster              //如果邻域内点不是核心点，并且无类别，比如噪音数据，则加入此类别
21          add P' to cluster C
22           
23 regionQuery(P, eps)                                       //计算邻域
24    return all points within P's eps-neighborhood
"""

#1.收集所有的数据点，确定维度
#2.将所有的数据点进行归类，判断哪些是核心点，哪些是边界点，哪些是噪声点
#3.去除所有的噪声点
#4.将可达的核心点相连接，形成簇

dim=0 #维度初始为0
def sumlist(lis):
    sumlis=0    
    for i in range(6):
        sumlis+=lis[i]
    return sumlis
    

def getData():# 获取看过电影次数的数据
    movieData=[]    
    f=open("E://DataMining//dbscanData.txt")
    for line in f:
        line=line.strip().split()
        line=[map(int, elem)[0] for elem in line]      
        sumline=sum(line)       
        line=[num/sumline for num in line]        
        movieData.append(line)  
   # print movieData
    dim=len(line)
    return movieData
#下面是关于DataFrame的一些文档
#http://www.cnblogs.com/chaosimple/p/4153083.html
#http://www.jianshu.com/p/8d156c0cd107
#iat可以用来专门提取末一个值
def getDataPandas():
    reader=pd.DataFrame() 
    reader= pd.read_table(r'.\dbscanData.txt',header=None,sep=' ')#iterator=True,chunksize=1000)    
    print reader
        
    #hello=reader.iloc[0]
    reader=reader.T     #转置   
    print reader    
    f3=lambda x: x/x.sum()
    reader=reader.apply(f3)
    reader=reader.T    #转回来
    print reader

    dbscan = cluster.DBSCAN(eps=0.3,min_samples=3,algorithm='brute',metric='euclidean')
    dbscan.fit(reader)
    res=dbscan.labels_
    print res
   # print reader[0]

minpoint=3
core=[]
boup=[]
noise=[]
eps=0.3

def defCore(movieData):
   # movieData=pd.DataFrame(movieData)
    #print movieData    
    i=0
    for point in movieData:
        count=0        
        for point2 in movieData:
            if dis(point,point2)<=eps:
                count+=1
                if count>minpoint:   
                    core.append(i);break
        i=i+1    
    i=0
    for point in movieData:    
        if i in core:
            continue
        j=0        
        for point2 in movieData:
            if j in core:
                if dis(point,point2)<= eps:
                    boup.append(i)
            j+=1
        i+=1    

    for i in range(len(movieData)):
        if i not in boup and i not in core:
            noise.append(i)
    #print noise
    
def dis(point,point2):
    
    distance=0    
    for i in range(len(point)):
        distance+=(point[i]-point2[i])**2
    distance=distance**0.5   
    return distance

def getCluster(movieData):
    #首先将第一个点初始化为第一个簇的起点    
    clus=[[0]]    
    i=1 #簇的下一个最大的标号 
    s=0
    for num in core[1:]:    #对于所有的点
        s=0        
        for clusNum in range(len(clus)):#对于所有现在聚好的类      
            for pn in clus[clusNum]:#对于现在类中的所有的点
                if dis(movieData[num],movieData[pn])<=eps:
                    if(s==0):                    
                        clus[clusNum].append(num);s=1
        if s == 0:
            clus.append([num])#如果都没有聚类成功，那么添加一个新的类
    print clus   

def main():
    getDataPandas()
    
      
   
''' 
    movieData=getData()
    defCore(movieData)
    getCluster(movieData)
'''


if __name__=="__main__":
    main()














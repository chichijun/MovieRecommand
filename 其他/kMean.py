# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 12:53:13 2016

@author: Administrator
"""

#参考 http://www.tuicool.com/articles/n2Y3IjF
from __future__ import division
import numpy as np
from sklearn.neighbors import NearestNeighbors
from itertools import combinations
import time
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from pylab import *

def sandian(distance):  
    #n = 1024  
    X = [i for i in range(1,len(distance)+1)] #np.random.normal(0, 1, n)  
    Y = distance#np.random.normal(0, 1, n)  
    T = np.arctan2(Y, X)  
    ax=axes([0.025, 0.025, 0.95, 0.95])
    ax.set_title("distance") 
    scatter(X, Y, s=75, c=T, alpha=.5)  
    xlim(0,len(distance)+1),
    xticks([i in range(1,len(distance)+1,100)])  
 #   ylim(0, distance[-1]),
    yticks([0.5,distance[-1],0.5])  
      #  i in range(0,distance[-1],0.5)
#    savefig('E://pythonProgram//DataMining//50wordso_ex.png', dpi=48)  
    show() 

def getData(fileName):# fileName='50words'获取看过电影次数的数据
    Data=[]    
    label=[]    
    f=open("E://DataMining//Data_collection4//"+fileName+"_TRAIN_PCA.csv")
    #f=open("E://DataMining//Data_collection1//"+fileName+"//"+fileName+"_MERGE_chosed")
    for line in f:
        line=line.strip().split(',')
        line=[eval(elem) for elem in line] # map(float, elem)[0]             
        label.append(line[-1])
        line=line[1:]        
        Data.append(line)  
    return label,Data


    
def getMaxAccurcy(value_k,label,X):           
    #db = DBSCAN(eps=epsilon, min_samples=min_points,metric='precomputed').fit(sim_matrix_d)#algorithm=, metric='euclidean').fit(X)#
    
    db= KMeans(n_clusters=value_k, random_state=0).fit(X)
    label=[i+1 for i in label]#让所有的label都是大一1的,实际的标签  
    
  #  print label    
    #留下的都是非噪声点
    actdbLabels=[]
    actlabels=[]
    count = 0
    for i in range(len(db.labels_)):
        if db.labels_[i]==-1:
            actdbLabels.append(db.labels_[i]+50+count)
            actlabels.append(label[i])
            count+=1
        else:
            actdbLabels.append(db.labels_[i])
            actlabels.append(label[i])
            
    if len(actdbLabels)==0:
        print "error"
        return 0
        
   # print "actlabels=%s"%actlabels
   # print "actdbLabels%s"%actdbLabels
    maxdbl=max(actdbLabels);maxl=max(actlabels)    
    mindbl=min(actdbLabels);minl=min(actlabels)    
    
    
    dbdic=[]#现在类标的字典
    ladic=[]#原来的类标的字典
    
    #统计类标向量的个数    
    matrix = [[0 for col in range(maxl+1)] for row in range(maxdbl+1)] 
    for i in range(len(actlabels)):
         matrix[actdbLabels[i]][actlabels[i]]+=1
  #  print len(matrix)
    #具体计算
    lineMaxAccuracy=[]    
    for i in range(mindbl,maxdbl+1):        
         acrsMax=0 
         for j in range(minl,maxl+1):
             acrs=2.0*matrix[i][j]/(actdbLabels.count(i)+actlabels.count(j))
             if acrs>acrsMax:
                 acrsMax=acrs
         lineMaxAccuracy.append(acrsMax)
   # print "lineMaxAccuracy=%s"%lineMaxAccuracy
    finalResult=sum(lineMaxAccuracy)/(maxdbl-mindbl+1)#这是最终的准确度
  #  print "finalResult=%.5spercent"%(finalResult*100)
    if finalResult==1.0:
        return 0
    return finalResult


if __name__ == '__main__':
    #fileNames2=['Two_Patterns','wafer','yoga']
    fileNames=['50words','Adiac','Beef','CBF','Coffee','ECG200','FaceAll','FaceFour','FISH','Gun_Point','Lighting2','Lighting7','OliveOil','SwedishLeaf','synthetic_control','Trace','Two_Patterns','wafer','yoga']
    for fileName in fileNames:    
        # 构建数据集
        label,Data=getData(fileName)
        X=Data    
       # 调试结果
        max_k=0
        max_accuracy=0;    
        for i in range(3,15,1):
                accuracy=getMaxAccurcy(i,label,X)
                if accuracy>max_accuracy:
                    max_accuracy=accuracy
                    max_k=i
        print "DataName=%s"%fileName
        print "max_accurcy=%s"%max_accuracy
        print "max_k=%s"%max_k
        print " "

    
    
    
    #需要统计每个类标有几个，原数据集类标和结果类标都要统计
    #需要map一下原来和结果类标，记录下个数，用二维数组表示吧，先算下最大最小类标
    #可以算了



















'''  
    centers = [37, 4]
    centers_2 = [-37, 4]
    X, labels_true = make_blobs(n_samples=100, centers=centers, cluster_std=20)
    print X    
    X_2, l_2 = make_blobs(n_samples=50, cluster_std=8, centers=centers_2)
    X = np.concatenate((X, X_2))
    print X
'''   


  
'''  
   # 构图
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    unique_labels = set(labels)
    colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = 'k'
        class_member_mask = (labels == k)
        xy = X[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=10)
        xy = X[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=6)
    plt.title('SNN')
    plt.show()
'''
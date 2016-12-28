# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:34:11 2016

@author: Administrator
"""
import linecache
from gensim import *
import numpy as np
from scipy import spatial
import gensim
import codecs
import os
from pylab import *
# code cs
# nultk

def methIndex():
    m=open("D:\\data0.txt") 	 #所有的方法都在这个文件当中了 #m=open(inputFile,'r')
    mapping={}
    i=0
    for line in m:
        mapping[i]=line.strip()  #记录文件当中的方法名，并且利用字典记录每个方法在文件当中的顺序 
        i=i+1
    m.close()
    return mapping		#mapping中记录了每个方法在文件当中的顺序 



def buildCorpus():       #######文本读到内存当中要用到设置缓存的方法(文本太大)
    corpus=[]
    for i in range(4800):
        line = linecache.getline(r"D:\\data2.txt",i)    #F:\\Programming\\ImpaceAnalysis\\MovieInforMation\\data1.txt            # print line
        corpus.append(line)     #虽然print出来的是是unicode编码，但是实际上是中文   #print "corpus=%s"%corpus[1] #只要这样就能正常读入
    texts=[[word for word in document.split()] for document in corpus]#.lower()返回将字符串中所有大写字符转换为小写后生成的字符串。
    dictionary = corpora.Dictionary(texts)       
    corpus = [dictionary.doc2bow(text) for text in texts]#记录了每个词对应的标号，以及出现的次数,这为后续算出概率做了准备
    return corpus,dictionary

#矩阵1    
def LSI(corpus,dictionary):
    tfidf=models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    lsi = models.LsiModel(corpus_tfidf,id2word=dictionary,num_topics=100)
    corpus_lsi = lsi[corpus_tfidf]
    lsiMatrix = []
    for i in corpus_lsi:
        temp = [0 for element in range(len(i))]
        for j in i:
            temp[j[0]]=j[1]
        lsiMatrix.append(temp)
    #np.savetxt(r'F:\Programming\ImpaceAnalysis\jEdit\LSIMovieMatrix.txt',lsiMatrix,fmt='%s')
    return lsiMatrix, lsi

#矩阵2
num_of_topics=200
def LDA(corpus,dictionary):
    tfidf=models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    lda = models.LdaModel(corpus_tfidf,id2word=dictionary,num_topics=100)
    lda_corpus = lda[corpus_tfidf]
    ldaMatrix = []
    for i in lda_corpus:
        temp = [0 for element in range(num_of_topics)]
        for j in i:
            temp[j[0]]=j[1]
        ldaMatrix.append(temp)
    return ldaMatrix, lda

#矩阵3    
class LabeledLineSentence(object):
    def __init__(self, filename):
        self.filename = filename
    def __iter__(self):
        for lid, line in enumerate(codecs.open(self.filename,encoding='utf-8')):
            yield gensim.models.doc2vec.LabeledSentence(words=line.split(), tags=[lid])
            
def model_generator(filename):
    #logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    lines = LabeledLineSentence(filename)
    model = gensim.models.doc2vec.Doc2Vec(lines, size=300, window=4, min_count=0, workers=4)
    return model



# 生成的
def queryLSI(lsi,queryData,dictionary):
    queryVector=[]
    vec_bow=dictionary.doc2bow(queryData.split())
    vec_query_lsi = lsi[vec_bow]
    tempQ=[0 for element in range(len(vec_query_lsi))]
    for k in vec_query_lsi:
        tempQ[int(k[0])]=k[1]
    if len(tempQ)!=0:
        queryVector.append(tempQ)
        #queryIDList.append(queryID.strip('.txt'))
    return queryVector
    
def queryLDA(lda,queryData,dictionary):
    queryVector=[]
    vec_bow=dictionary.doc2bow(queryData.split())
    vec_query_lda= lda[vec_bow]
    tempQ=[0 for element in range(num_of_topics)]
    for k in vec_query_lda:
        tempQ[int(k[0])]=k[1]
    if len(tempQ)!=0:
        queryVector.append(tempQ)
        #queryIDList.append(queryID.strip('.txt'))
    return queryVector
    
def query2vector(query,model):
#将query转化成为向量，并存储于文件vectorfile中
    queryMatrix=[]
    wordlist = query.split()
    #print "hello%s"%model[wordlist[2]]
    vector = []
    for i in range(0,len(wordlist)):
        try:
            vector.append(model[wordlist[i]])
        except:
            print "No word "+wordlist[i]
    sum = [0]*300
    for i in range (0,len(vector)):
        for j in range(0,len(sum)):
            sum[j]=sum[j]+vector[i][j]            
    for i in range (0,len(sum)):
        if len(vector)!=0:
            sum[i] = sum[i]/len(vector)
    queryMatrix.append(sum)
    return queryMatrix
    
def getResult(matrix,queryVector):#irMatrix=930×100，即930个方法,100个主题
    matrix=matrix[1:]   # 这里是解决数据处理上的一些问题
    matrix=np.array(matrix)
    #print matrix    
    np.savetxt(r'D:\theLSIFrmMatrix.txt',matrix,fmt='%s')
    queryVector=queryVector[0]
    rankMatrix=np.zeros((1,matrix.shape[0]))
    for i in range(matrix.shape[0]):
        rankMatrix[0][i] = 1-spatial.distance.cosine(matrix[i,:],queryVector)
            #rankMatrix矩阵的shape是(6413, 248)。其中6431个方法向量，248个query向量        
            #np.savetxt(r'F:\Programming\ImpaceAnalysis\jEdit\similarRankFile.txt',rankMatrix,fmt='%s')
    return list(rankMatrix[0])
    

    
def maine(querySegs):  
    mapping=methIndex() #根据序号确定的电影名
    corpus,dictionary=buildCorpus()#对于所有电影信息的语料建立就直接用行数来进行就可以了
    queryData=querySegs
    queryID=1
    result={}    
    lsiMatrix, lsi= LSI(corpus,dictionary)
    queryVector=queryLSI(lsi,queryData,dictionary)
    rankLsiMatrix=getResult(lsiMatrix,queryVector) 
    result[queryID]=np.argsort(-(np.array(rankLsiMatrix)))[0:10]#argsort返回数组值从小到大的索引值，因为其中的rank矩阵前面加了负号，所以实际上是从大到小的排列
    rank=(np.array(rankLsiMatrix))[0:10]
    results=result[queryID]
    #shanXing(rank,result)    
    return rank,results,mapping
 


def query(querySegs):
    resultTemp = ''
    resultList = []
    rank,result,mapping=maine(querySegs)
    
    for i in range(0, 10):
        resultTemp = u"测试结果" + str(i)
        resultList.append(resultTemp)
        
    return rank,result,mapping

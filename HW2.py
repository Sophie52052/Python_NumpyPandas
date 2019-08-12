# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 00:03:27 2019

@author: Sophie
"""



import time
import pandas as pd
iris = pd.read_csv('iris.csv')

a1=iris.iloc[:, 0:4]
a2=iris.iloc[:, 0:4]
def walk_row(row):
    print(type(row))
    print(row)
#apply
tStart1 = time.time()#計時開始
test=a1.apply(walk_row, axis=0)
tEnd1 = time.time()#計時結束
print ("'Apply' cost %f sec" % (tEnd1 - tStart1))#自動進位

#itertuples
tStart2 = time.time()#計時開始
for ir in iris.itertuples(): 
    print(ir)
tEnd2 = time.time()#計時結束
print ("'Itertuples' cost %f sec" % (tEnd2 - tStart2))#自動進位

#Answerishere~~~~
iris.columns = ['A', 'B', 'C', 'D', 'class'] 
#sample = iris.sample(n=10)
def text_function(row):
    return 'class: {class}, A:{A},B:{B},C:{C},D:{D}'.format(**row.to_dict())
tStart1 = time.time()#計時開始
print(iris.apply(text_function, axis=1))
tEnd1 = time.time()#計時結束
print ("'Apply' cost %f sec" % (tEnd1 - tStart1))#自動進位

iris.columns = ['A', 'B', 'C', 'D', 'class'] 
#sample = iris.sample(n=10)
tStart2 = time.time()#計時開始
for ir in iris.itertuples():
    print(ir)
tEnd2 = time.time()#計時結束
print ("'Itertuples' cost %f sec" % (tEnd2 - tStart2))#自動進位


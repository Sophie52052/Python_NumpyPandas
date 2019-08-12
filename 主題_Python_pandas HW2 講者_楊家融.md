# 主題:Python/pandas HW2 講者:楊家融

Q1.Why we should avoid using itertuples?

Design a simple function to work on one line Compare the difference in speed between apply and itertuples

A1.
```
import time
import pandas as pd
iris = pd.read_csv('iris.csv')


#apply
tStart1 = time.time()#計時開始
iris.iloc[:, 0:4].apply(sum, axis=1)
tEnd1 = time.time()#計時結束
print ("'Apply' cost %f sec" % (tEnd1 - tStart1))#自動進位

#itertuples
tStart2 = time.time()#計時開始
for ir in iris.itertuples(): 
    iris.iloc[:, 0:4]
tEnd2 = time.time()#計時結束
print ("'Itertuples' cost %f sec" % (tEnd2 - tStart2))#自動進位
```
```
output:
'Apply' cost 0.005025 sec
'Itertuples' cost 0.035527 sec
```
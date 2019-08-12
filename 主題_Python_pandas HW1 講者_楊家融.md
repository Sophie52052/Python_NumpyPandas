# 主題:Python/pandas HW1 講者:楊家融

Q1. Tell the difference of the two files: iris.csv and iris_output.csv

![](https://i.imgur.com/vP7Hvgp.png)



多了index欄位，自動產生編號

<br>

Q2. How two save the dataframe to iris_output.csv exactly the same with iris.csv

![](https://i.imgur.com/7mzL4dg.png)



```
import pandas as pd
iris = pd.read_csv('iris.csv')
iris.to_csv('iris_output1.csv', index = False)
```
加入index=False
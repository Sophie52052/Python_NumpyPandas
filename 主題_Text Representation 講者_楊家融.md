# 主題:Text Representation 講者:楊家融

1.Estimate the time for training the word2vec model with today’s English Wikipedia on your computer

* Check genism
* Get the training data on the same page (text8)
* https://radimrehurek.com/gensim/models/word2vec.html
* http://mattmahoney.net/dc/textdata.html

```
#use Google Colab

import time
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import word2vec
from gensim.models.word2vec import Text8Corpus
import logging

tStart1 = time.time()#計時開始
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = Text8Corpus('text8')
model = word2vec.Word2Vec(sentences, size=200)
tEnd1 = time.time()#計時結束

print ("'Cost %f sec" % (tEnd1 - tStart1))#自動進位

model.save("word2vec.model")
```
> 2019-07-30 06:29:45,868 : INFO : EPOCH 1 - PROGRESS: at 2.88% examples, 353158 words/s, in_qsize 5, out_qsize 0
2019-07-30 06:29:46,892 : INFO : EPOCH 1 - PROGRESS: at 5.82% examples, 353285 words/s, in_qsize 5, out_qsize 0
...
2019-07-30 06:32:39,532 : INFO : EPOCH 5 - PROGRESS: at 95.06% examples, 355092 words/s, in_qsize 5, out_qsize 0
2019-07-30 06:32:40,534 : INFO : EPOCH 5 - PROGRESS: at 97.94% examples, 355134 words/s, in_qsize 5, out_qsize 0
...
Cost 184.574123 sec



2.How to estimate the time used on your computer to train with full English Wikipedia


* Try Wikipedia Statistics page https://en.wikipedia.org/wiki/Wikipedia:Size_in_volumes

>Google Colab: 
 text8-- 1.7 million words -- 3 mins
 Wikipedia-- 3.65 billion words --?
 ? -- 4.5 days
 Mycomputer:
 text8-- 1.7 million words -- 3 mins
 Wikipedia-- 3.65 billion words --?
 ? -- 1 month



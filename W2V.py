# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:03:03 2019

@author: Sophie
"""

from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import word2vec
from gensim.models.word2vec import Text8Corpus
import logging
#path = get_tmpfile("word2vec.model")
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#model = Word2Vec(common_texts, size=100, window=5, min_count=1, workers=4)
#model.save("word2vec.model")
sentences = Text8Corpus('text8')
model = word2vec.Word2Vec(sentences, size=40)
model.save("word2vec.model")
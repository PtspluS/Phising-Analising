import numpy as np
import pandas as pd # Clement
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
from Email import Email
from nltk.stem.snowball import SnowballStemmer

mail = open("../mail_0.txt",'r')

email = Email(mail.read())

text = "Hi, I am a bitch"

stemmer = SnowballStemmer("english")

token = nltk.word_tokenize(text)
stopwords = nltk.corpus.stopwords.words('english')

tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
filtered_tokens = []
# filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
for token in tokens:
    if re.search('[a-zA-Z]', token):
        filtered_tokens.append(token)
print(tokens)
print(filtered_tokens)




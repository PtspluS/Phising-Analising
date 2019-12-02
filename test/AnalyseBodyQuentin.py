import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3

import sys
sys.path.append('../')
from src.Email import *

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

liste_email = ['email1.txt','email2.txt']

email = list()


def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens


def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

mails = list()
for mail in liste_email:
    email = list()
    file  = open(mail,'r')
    texte = file.read()


    email.append(Email(texte).get_text())
    
    mails.append(email)
    file.close()

print(mails)
stopwords = nltk.corpus.stopwords.words('english')

while "nbsp" in mails[0]:
    mails[0][0].remove("nbsp")

while "nbsp" in mails[1]:
    mails[0][0].remove("nbsp")

liste1 = tokenize_only(mails[0][0])
liste2 = tokenize_only(mails[1][0])

while "nbsp" in liste1:
    liste1.remove("nbsp")

while "nbsp" in liste2:
    liste2.remove("nbsp")

print(liste1, liste2, sep='\n')

"""
for mail in mails:
    print(mail)
    while 'nbsp' in mail:
        mail.remove('nbsp')

print(mails)


indice = 1
for mail in email:
    totalvocab_stemmed = []
    totalvocab_tokenized = []
    
    allwords_stemmed = tokenize_and_stem(mail) #for each item in 'synopses', tokenize/stem
    totalvocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list
        
    allwords_tokenized = tokenize_only(mail)
    totalvocab_tokenized.extend(allwords_tokenized)

vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
print( 'there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame')
"""

# -*- coding: utf-8 -*-
"""
la fonction analyse retourne un tableau de taille 2 contenant le resultat du champs lexical critique (0) et champs lexical action (1)
"""

import pandas as pd
import spacy
spacy.load('en_core_web_sm')


from spacy.lang.en import English
parser = English()


def tokenize(text):
    lda_tokens = []
    tokens = parser(text)
    for token in tokens:
        if token.orth_.isspace():
            continue
        elif token.like_url:
            lda_tokens.append('URL')
        elif token.orth_.startswith('@'):
            lda_tokens.append('SCREEN_NAME')
        else:
            lda_tokens.append(token.lower_)
    return lda_tokens

import nltk


from nltk.corpus import wordnet as wn

def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma
    
from nltk.stem.wordnet import WordNetLemmatizer

def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)


en_stop = set(nltk.corpus.stopwords.words('english'))


def simplify_text(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in en_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens

from gensim import corpora
import gensim
import pickle

def analyseCritique(text):

    #text = text.lower()
    compteur = 0

    mon_fichier = open("../data/lexico/critique.txt", "r")
    critique = mon_fichier.read()
    mon_fichier.close()

    critique = critique.split(';')
    
    tabText = text#.split(' ')
    
    for i in range(len(tabText)):
        
        for j in range(len(critique)):
            
            if tabText[i] == critique[j]:
                
                compteur = compteur + 1  
                
                #print(tabText[i])
    
    return compteur

def analyseAction(text):
    
    compteur = 0
    
    #text = text.lower()
    
    mon_fichier = open("../data/lexico/action.txt", "r")
    action = mon_fichier.read()
    mon_fichier.close()

    action = action.split(';')
    
    tabText = text#.split(' ')
    
    for i in range(len(tabText)):
        
        for j in range(len(action)):
            
            if tabText[i] == action[j]:
                
                compteur = compteur + 1  
                
                #print(tabText[i])
    
    return compteur

def analyseLexico(text):
    
    return [analyseCritique(text), analyseAction(text)]

def run():
    text ="""
    PUBLIC ANNOUNCEMENT:

    The new domain names are finally available to the general public at discount prices. Now you can register one of the exciting new .BIZ or .INFO domain names, as well as the original .COM and .NET names for just $14.95. These brand new domain extensions were recently approved by ICANN and have the same rights as the original .COM and .NET domain names. The biggest benefit is of-course that the .BIZ and .INFO domain names are currently more available. i.e. it will be much easier to register an attractive and easy-to-remember domain name for the same price.  Visit: http://www.affordable-domains.com today for more info.
     
    Register your domain name today for just $14.95 at: http://www.affordable-domains.com/  Registration fees include full access to an easy-to-use control panel to manage your domain name in the future.
     
    Sincerely,
     
    Domain Administrator
    Affordable Domains


    To remove your email address from further promotional mailings from this company, click here:
    """
    print(simplify_text(text))
    print(analyseLexico(simplify_text(text)))

run()

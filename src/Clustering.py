import numpy as np
import pandas as pd # Clement
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
from Email_extractor import extract_text_full, find_language

mail = open("../mail_0.txt",'r')
mail_text = extract_text_full(mail)
lang = find_language(mail)

if lang == 'EN':
    pass

def En_clustering():
    pass


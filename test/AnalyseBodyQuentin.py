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

liste_email = ['email1.txt','email2.txt']
print("ici1")
for mail in liste_email:
    file  = open(mail,'r')
    email = Email(file.read())
    file.close()

print("ici2")
print(email.get_text())

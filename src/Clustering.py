import numpy as np
import pandas as pd # Clement
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
from Email import Email

mail = open("../mail_0.txt",'r')

email = Email(mail.read())

print(email.get_text())



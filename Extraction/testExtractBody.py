# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:44:29 2019

@author: Toine
"""

import Extraction;

mon_fichier = open("mailsTest/email2.txt");
data = mon_fichier.read();
mon_fichier.close();

print(Extraction.extractTexte(data));
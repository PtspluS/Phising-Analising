# -*- coding: utf-8 -*-
"""
retourne un tableau
"""

def analyseObjet(objet):
    
    longeur = len(objet)
    rep = 1;
    
    if objet.find("RE :") != -1 or objet.find("RE:") != -1:
        
        rep = 0
            
    
    return [longeur, rep]


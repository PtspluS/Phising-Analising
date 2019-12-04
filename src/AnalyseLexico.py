# -*- coding: utf-8 -*-
"""
la fonction analyse retourne un tableau de taille 2 contenant le resultat du champs lexical critique (0) et champs lexical action (1)
"""

def analyseCritique(text):
    
    compteur = 0

    mon_fichier = open("../data/lexico/critique.txt", "r")
    critique = mon_fichier.read()
    mon_fichier.close()

    critique = critique.split(';')
    
    tabText = text.split(' ')
    
    for i in range(len(tabText)):
        
        for j in range(len(critique)):
            
            if tabText[i] == critique[j]:
                
                compteur = compteur + 1  
                
                #print(tabText[i])
    
    return compteur

def analyseAction(text):
    
    compteur = 0

    mon_fichier = open("../data/lexico/action.txt", "r")
    action = mon_fichier.read()
    mon_fichier.close()

    action = action.split(';')
    
    tabText = text.split(' ')
    
    for i in range(len(tabText)):
        
        for j in range(len(action)):
            
            if tabText[i] == action[j]:
                
                compteur = compteur + 1  
                
                #print(tabText[i])
    
    return compteur

def analyseLexico(text):
    
    return [analyseCritique(text), analyseAction(text)]



# -*- coding: utf-8 -*-
import re


def rechercheMot(chaine, fichier, longeur):
    
    mon_fichier = open(fichier)
    listePrenom = mon_fichier.read()
    mon_fichier.close()
    
    motTrouve = ""
    
    for i in range(len(chaine)):
    
        for j in range(len(chaine)):
        
            if j > i - 1:
        
                newCutChaine = chaine[i:j + 1]
        
                recherche = re.search(r""+str(newCutChaine)+"", listePrenom, re.MULTILINE)
        
                if recherche and len(recherche.group()) > longeur - 1 and len(recherche.group()) > len(motTrouve):
                
                    motTrouve = recherche.group()
    
    
    return motTrouve



def creationListeMotsAdresse(adresse, fichier):

    adressePropreTab = adresse.split("@")
    
    adressePropre = str(adressePropreTab[0]) + str(adressePropreTab[1])
    
    tab = adressePropre.split(".")

    

    longeur = len(tab)
    
    

    i = 0
    
    while i < longeur:
    
        
        motTrouve = rechercheMot(tab[i], fichier, 3)
    
            
        if motTrouve != tab[i] and len(motTrouve) > 2:
            
                    
            tab[i] = tab[i].split(motTrouve)
        
            tab.append(motTrouve)
        
            longeur  = longeur + len(tab[i])
        
            for j in range(len(tab[i])):
            
                tab.append(tab[i][j])
                    
            del tab[i]
        
        
            i = i - 1
        
        if len(motTrouve) < 3:
        
            tab[i] = False
        
        i = i + 1
        
        
    return tab





def extention(adresse):
    
    membreDroite = adresse.split("@")[1]
    
    membreDroiteTab = membreDroite.split(".")
    
    return membreDroiteTab[len(membreDroiteTab) - 1]



def creationListeMotsNom(nom, fichier):

    
    
    tab = nom.lower().split(".")

    

    longeur = len(tab)
    
    

    i = 0
    
    while i < longeur:
    
        
        motTrouve = rechercheMot(tab[i], fichier, 3)
    
            
        if motTrouve != tab[i] and len(motTrouve) > 2:
            
                    
            tab[i] = tab[i].split(motTrouve)
        
            tab.append(motTrouve)
        
            longeur  = longeur + len(tab[i])
        
            for j in range(len(tab[i])):
            
                tab.append(tab[i][j])
                    
            del tab[i]
        
        
            i = i - 1
        
        if len(motTrouve) < 3:
        
            tab[i] = False
        
        i = i + 1
        
        
    return tab



def analyseComparaisonNomAdresse(nom, adresse):
    
    compteur = 0
    
    for i in range(len(nom)):
        
        for j in range(len(adresse)):
            
            if nom[i] != False and nom[i] == adresse[j]:
                
                compteur = compteur + 1
    
    
    return compteur




def analyseExtention(extention, listeNom):
    
    mon_fichier = open("wordlist/extensions.txt", encoding="utf8")
    listeExtensions = mon_fichier.read()
    mon_fichier.close()
    comparaisonExtention = 0
    extentionSafe = 0
      
    recherche = re.search(r""+str(extention)+"$", listeExtensions, re.MULTILINE)
        
               
    if recherche:
        
        if extention == recherche.group(0):
            
                       
            extentionSafe = 1
            
    if extentionSafe == 0:
            
            
            tabUnitaire = [0]
    
            tabUnitaire[0] = extention
    
    
            comparaisonExtention = analyseComparaisonNomAdresse(tabUnitaire, listeNom)
    
   
        
    return extentionSafe + comparaisonExtention


def analyseSignification(listeAdresseGauche):
    
    listeMot = listeAdresseGauche
    
    compteur = 0
    
    for i in range(len(listeMot)):
        
        if listeMot[i] != False:
            
            compteur = compteur + 1
            
    
    
    return compteur
    




def analyse(nom, adresse):
    """

    :param nom: nom de l'envoyeur
    :param adresse: adresse email de l'envoyeur
    :return:
    """

    listeAdresse = creationListeMotsAdresse(adresse, "../data/wordlist/francais-prenoms.txt") + creationListeMotsAdresse(adresse, "../data/wordlist/words.txt") + creationListeMotsAdresse(adresse, "../data/wordlist/entreprises.txt")
    listeNom = creationListeMotsNom(nom, "../data/wordlist/francais-prenoms.txt") + creationListeMotsNom(nom, "../data/wordlist/words.txt") + creationListeMotsAdresse(adresse, "../data/wordlist/entreprises.txt")
    listeAdresseGauche = creationListeMotsNom(adresse.split("@")[0], "../data/wordlist/francais-prenoms.txt") + creationListeMotsNom(adresse.split("@")[0], "../data/wordlist/words.txt") + creationListeMotsNom(adresse.split("@")[0], "../data/wordlist/entreprises.txt")

    comparaisonAnalyse = analyseComparaisonNomAdresse(listeNom, listeAdresse)# compteur
    extentionAnalyse = analyseExtention(extention(adresse), listeNom)# binaire
    significationAnalyse = analyseSignification(listeAdresseGauche)# compteur
        
                   
    return [extentionAnalyse, comparaisonAnalyse, significationAnalyse]


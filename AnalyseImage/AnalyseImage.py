# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:09:40 2019

@author: Toine
"""


def analyseLien(tabLien, nom):
    
    ratio = 0;
    nombreLiens = len(tabLien);
    nombreLiensConformes = 0;
    lien = "";
    
    if nombreLiens > 0: 
        
        for i in range(len(tabLien)):
        
            lien = tabLien[i];
            
            if (lien.find(nom) != -1):
                
                nombreLiensConformes = nombreLiensConformes + 1;

        ratio = nombreLiensConformes / nombreLiens;
    
    return ratio;


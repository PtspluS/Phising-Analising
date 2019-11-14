# -*- coding: utf-8 -*-
"""

La fonction analyseLien retourne un nombre entre 0 et 1

"""


def analyseLien(tabLien, nom):
    
    ratio = 0;
    nombreLiens = len(tabLien);
    nombreLiensConformes = 0;
    lien = "";
    
    if nombreLiens > 0: 
        
        for i in range(len(tabLien)):
        
            lien = tabLien[i];
            
            if (lien.lower().find(nom.lower()) != -1):
                
                nombreLiensConformes = nombreLiensConformes + 1;

        ratio = nombreLiensConformes / nombreLiens;
    
    return ratio;

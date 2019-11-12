# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:52:22 2019

@author: Toine
"""

import Extraction;
import AnalyseSource;

def analyseSource(filename):

    mon_fichier = open(filename, "r");
    data = mon_fichier.read();
    mon_fichier.close();
    
    result = 3;
    
    sourceNom = Extraction.extractSourceNom(data);

    sourceAdresse = Extraction.extractSourceAdresse(data);
    
    tabAnalyse = AnalyseSource.analyse(sourceNom, sourceAdresse);
    
    if(tabAnalyse[1] == 0):
        
        result = 2
        
        if (tabAnalyse[2] == 0):
            
            result == 1;
            
    if (tabAnalyse[2] == 0 and tabAnalyse[1] != 0):
            
            result == 2;
            
    return result;

# -*- coding: utf-8 -*-

import AnalyseSource

adresse ="antoine.g2210@gmail.com";
nom ="Antoine Genonceau";

tabAdresse =["qboens@hotmail.fr", "uber@uber.com","bonsplans@newsletter.oui.sncf", "no-reply@duolingo.com", "no-reply@stellarprofits.top", "zVjR59572l@amazongiftreward.com"];
tabNom =["Quentin Bons", "Uber Eats", "OUI.sncf", "Duolingo", "Keto Shark Tank", "Récompenses Amazon"];

for i in range(len(tabAdresse)):
    
    tabAnalyse = AnalyseSource.analyse(tabNom[i], tabAdresse[i])
    
    print("Nom :", tabNom[i],"Adresse :", tabAdresse[i],"Analyse :", "Signification :", tabAnalyse[2], "Comparaison", tabAnalyse[1], "Extention",tabAnalyse[0]);
    

# coding: utf-8
import Partition;
import re;


mon_fichier = open("email0.txt", "r");
data = mon_fichier.read();
mon_fichier.close();

    
Body = Partition.body(data);


print(Partition.texte(Partition.body(data)));


newCut = re.sub(r"<[^>]*>", "", Body, re.UNICODE);






supLine = re.sub(r"[\n]", "", newCut);


#print(supLine);


#accentAigu = re.sub(r"=C3=A9", "é", supLine);


#uChapeau = re.sub(r"=C3==BB", "û", accentAigu);



#egale20 = re.sub(r"=20", "", uChapeau);



#print(egale20);





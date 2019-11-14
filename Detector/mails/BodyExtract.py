# coding: utf8
import Partition
import re
from codecs import open
import quopri



mon_fichier = open("email1.txt", encoding="utf8")
data = mon_fichier.read()
mon_fichier.close()

    
Body = Partition.body(data)


newCut = re.sub(r"<[^>]*>", "", Body)

quopri.a2b_qp = quopri.b2a_qp = None

chaineB = quopri.decodestring(bytes(newCut,encoding="utf-8"))

chaine = str(chaineB, encoding="utf-8")

print(chaine)

#cut = bytes(newCut, encoding="ascii")



#chaine = str(cut, encoding="utf-8")





#supLine = re.sub(r"[\n]", "", newCut)


#print(supLine)


#accentAigu = re.sub(r"=C3=A9", "é", supLine)


#uChapeau = re.sub(r"=C3==BB", "û", accentAigu)



#egale20 = re.sub(r"=20", "", uChapeau)



#print(egale20)





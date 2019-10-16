# coding: utf8
import Partition;
import re;
from codecs import open;
import quopri


#<<<<<<< Updated upstream
def BodyExtract(fichier):
    mon_fichier = open(fichier, encoding="utf8");

    data = mon_fichier.read();
    mon_fichier.close();

        
    Body = Partition.body(data);

    newCut = re.sub(r"<[^>]*>", "", Body);

    quopri.a2b_qp = quopri.b2a_qp = None;

    chaineB = quopri.decodestring(bytes(newCut,encoding="utf-8"));

    chaine = str(chaineB, encoding="utf-8");

    return chaine;

"""
newCut = re.sub(r"<[^>]*>", "", Body, re.UNICODE);
>>>>>>> Stashed changes

#chaine = str(cut, encoding="utf-8");





#supLine = re.sub(r"[\n]", "", newCut);


#print("\n",supLine);


accentAigu = re.sub(r"=C3=A9", "é", supLine);


uChapeau = re.sub(r"=C3==BB", "û", accentAigu);



egale20 = re.sub(r"=20", "", uChapeau);



#print("\n\n",egale20);

"""



import Partition


#Exemple utilisation des fonctions partition



mon_fichier = open("email.txt", "r");
data = mon_fichier.read();
mon_fichier.close();



print("Norme :");

print(Partition.norme(Partition.typeMail(Partition.header(data))));

print("Adresse Source :");

print(Partition.sourceAdresse(Partition.source(Partition.header(data))));
import Partition

mon_fichier = open("email.txt", "r");
data = mon_fichier.read();
mon_fichier.close();

print(Partition.body(data));
import Partition


#Exemple utilisation des fonctions partition




def extractionPrint(filename):

    mon_fichier = open(filename, "r");
    data = mon_fichier.read();
    mon_fichier.close();
    
    


    header = Partition.header(data);

    date = Partition.date(header);

    source = Partition.source(header);

    destination = Partition.destination(header);

    typeMail =Partition.typeMail(header);

    topic = Partition.topic(header);

    objet = Partition.objet(header);

    encodageTransfert = Partition.encodageTransfert(header);

    sourceNom = Partition.sourceNom(source);

    sourceAdresse = Partition.sourceAdresse(source);

    destinationNom = Partition.destinationNom(destination);

    destinationAdresse = Partition.destinationAdresse(destination);

    langage = Partition.langage(typeMail);

    norme = Partition.norme(typeMail);


    print("Date :")

    print(date, "\n");

    print("objet :");

    print(objet, "\n");

    print("Adresse Source :");

    print(sourceAdresse, "\n");

    print("Nom Source :");

    print(sourceNom, "\n");

    print("Adresse Destination :");

    print(destinationAdresse, "\n");

    print("Nom Destination :");

    print(destinationNom, "\n");

    print("Topic :");

    print(topic, "\n")

    print("Encodage de Transfert: ");

    print(encodageTransfert, "\n");

    print("Langage :")

    print(langage, "\n");

    print("Norme :");

    print(norme, "\n");


print("Extraction de mail 0: \n");
extractionPrint("email.txt");
print("\n\n\n");


print("Extraction de mail 1: \n");
extractionPrint("email1.txt");
print("\n\n\n");


print("Extraction de mail 2: \n");
extractionPrint("email2.txt");
print("\n\n\n");

print("Extraction de mail 3: \n");
extractionPrint("email3.txt");
print("\n\n\n");

print("Extraction de mail 0: \n");
extractionPrint("email0.txt");
print("\n\n\n");
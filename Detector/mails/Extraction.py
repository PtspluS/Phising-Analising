import Partition


#Exemple utilisation des fonctions partition


def extractDate(data):
    
    return Partition.date(Partition.header(data));
    
def extractTopic(data):
    
    return Partition.topic(Partition.header(data));
    
def extractSourceNom(data):
    
    return Partition.sourceNom(Partition.source(Partition.header(data)));
    
def extractSourceAdresse(data):
    
    return Partition.sourceAdresse(Partition.source(Partition.header(data)));
    
def extractDestinationNom(data):
    
    return Partition.destinationNom(Partition.destination(Partition.header(data)));
    
def extractDestinationAdresse(data):
    
    return Partition.destinationAdresse(Partition.destination(Partition.header(data)));
    
def extractLangage(data):
    
    return Partition.langage(Partition.typeMail(Partition.header(data)));
    
def extractNorme(data):

    return Partition.norme(Partition.typeMail(Partition.header(data)));
    
def extractObjet(data):
    
    return Partition.objet(Partition.header(data));
    
def extractEncodageTransfert(data):

    return Partition.encodageTransfert(Partition.header(data));
    
    
    
    
    
    
def extractionHeaderPrint(filename):

    mon_fichier = open(filename, "r");
    data = mon_fichier.read();
    mon_fichier.close();
    
       

    date = extractDate(data);  
    
    topic = extractTopic(data);

    objet = extractObjet(data);

    encodageTransfert = extractEncodageTransfert(data);

    sourceNom = extractSourceNom(data);

    sourceAdresse = extractSourceAdresse(data);

    destinationNom = extractDestinationNom(data);

    destinationAdresse = extractDestinationAdresse(data);

    langage = extractLangage(data);

    norme = extractNorme(data);


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



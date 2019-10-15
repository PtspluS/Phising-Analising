import re;


def partition(mail, balise):

   
    partie = "";

    if balise == "header":       
        
        header = re.match(r"^((.|\n)*)<html>", mail);     
        partie = header.group(1);
        
    if balise == "head":

        head = re.match(r"^((.|\n)*)<html>((.|\n)*)<body>", mail);
        partie = head.group(3);
    
    if balise == "body":

        body = re.match(r"^((.|\n)*)<body>((.|\n)*)</body>", mail);
        partie = body.group(3);

    return partie;


def body(mail):
    
    return partition(mail, "body");

def head(mail):
    
    return partition(mail, "head");

def header(mail):
    
    return partition(mail, "header");

def date(header):
    
    date = re.match(r"^((.|\n)*)Date: ((.|\n)*)From", header);
    
    return date.group(3);

def source(header):
    
    source = re.match(r"^((.|\n)*)From: ((.|\n)*)Subject", header);
    
    return source.group(3);

def sourceAdresse(source):
    
    sourceAdresse = re.match(r"^((.|\n)*)<((.|\n)*)>", source);
    
    return sourceAdresse.group(3);

def sourceNom(source):
    
    sourceNom = re.match(r"((.|\n)*) <", source);
    
    return sourceNom.group(1);

def objet(header):
    
    objet = re.match(r"^((.|\n)*)Subject:((.|\n)*)Thread-Topic", header);
    
    return objet.group(3);

def topic(header):
    
    topic = re.match(r"^((.|\n)*)Topic:((.|\n)*)To: ", header);
    
    return topic.group(3);


def destination(header):
    
    destination = re.match(r"^((.|\n)*)To: ((.|\n)*)Content-Transfer-Encoding: ", header);
    
    return destination.group(3);

def destinationAdresse(destination):
    
    destinationAdresse = re.match(r"^((.|\n)*)<((.|\n)*)>", destination);
    
    return destinationAdresse.group(3);

def destinationNom(destination):
    
    destinationNom = re.match(r"((.|\n)*) <", destination);
    
    return destinationNom.group(1);


def encodageTransfert(header):
    
    encodageTransfert = re.match(r"^((.|\n)*)Content-Transfer-Encoding: ((.|\n)*)Content-Type: ", header);
    
    return encodageTransfert.group(3);


def typeMail(header):
    
    typeMail = re.match(r"^((.|\n)*)Content-Type: ((.|\n)*)$", header);
    
    return typeMail.group(3);

def langage(typeMail):
    
    langage = re.match(r"((.|\n)*);", typeMail);
    
    return langage.group(1);

def norme(typeMail):  
    
    norme = re.match(r"((.|\n)*); ((.|\n)*)$", typeMail, re.MULTILINE);
    
    return norme.group(3);



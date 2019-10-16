import re;


def partition(mail, balise):

   
    partie = "";

    if balise == "header":       
        
        header = re.match(r"^((.|\n)*)<html.", mail);     
        partie = header.group(1);
        
    if balise == "head":

        head = re.match(r"^((.|\n)*)<head>((.|\n)*)</head>", mail);
        partie = head.group(3);
    
    if balise == "body":

        body = re.match(r"^((.|\n)*)</head>((.|\n)*)</body>", mail);
        partie = body.group(3);

    return partie;


def body(mail):
    
    return partition(mail, "body");

def head(mail):
    
    return partition(mail, "head");

def header(mail):
    
    return partition(mail, "header");

def date(header):
    
    date = re.match(r"^((.|\n)*)Date: ((.)*)", header);
    
    return date.group(3);

def source(header):
    
    source = re.match(r"^((.|\n)*)From: ((.)*)", header);
    
    return source.group(3);

def sourceAdresse(source):
    
    sourceAdresse = re.match(r"^((.|\n)*)<((.|\n)*)>", source);
    
    return sourceAdresse.group(3);

def sourceNom(source):
    
    sourceNom = re.match(r"((.|\n)*) <", source);
    
    return sourceNom.group(1);

def objet(header):
          
    objet = re.match(r"^((.|\n)*)Subject:((.)*)\n", header);
    
    objetTemp = objet.group(3);

    
    if len(objetTemp) < 2:
        
        newTemp = re.match(r"^((.|\n)*)Subject:\n ((.)*)", header);
        
        objetTemp = newTemp.group(3); 
    
    return objetTemp;

def topic(header):
    
    topic = re.match(r"^((.|\n)*)Topic:((.)*)", header);
    
    topicTemp = topic.group(3);
    
    if len(topicTemp) < 2:
        
        newTemp = re.match(r"^((.|\n)*)Topic:\n ((.)*)", header);
        
        topicTemp = newTemp.group(3); 
    
    return topicTemp;


def destination(header):
    
    destination = re.match(r"^((.|\n)*)\nTo:((.)*)", header);
    
    return destination.group(3);

def destinationAdresse(destination):
    
    destinationAdresse = re.match(r"^((.|\n)*)<((.|\n)*)>", destination);
    
    return destinationAdresse.group(3);

def destinationNom(destination):
    
    destinationNom = re.match(r' "((.)*)"', destination);
    
    return destinationNom.group(1);


def encodageTransfert(header):
    
    encodageTransfert = re.match(r"^((.|\n)*)Content-Transfer-Encoding: ((.)*)", header);
    
    return encodageTransfert.group(3);


def typeMail(header):
    
    typeMail = re.match(r"^((.|\n)*)Content-Type: ((.)*)", header);
    
    return typeMail.group(3);

def langage(typeMail):
    
    langage = re.match(r"((.|\n)*);", typeMail);
    
    return langage.group(1);

def norme(typeMail):  
    
    norme = re.match(r'((.)*)"((.)*)"', typeMail, re.MULTILINE);
    
    return norme.group(3);



###############################################################################
    

def texte(body):
    
    newCut = re.sub(r"<[^>]*>", "", body);

    supLine = re.sub(r"[\n]", "", newCut);

    return supLine;








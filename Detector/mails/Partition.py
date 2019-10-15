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



    



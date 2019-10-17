import re


'''
extract_header(plainText_email : str)
    extract the header part of the email
    return : 
        - return the header (str)
'''
def extract_header(plainText_email):
    header = re.findall("(.+\n+)+</head>", plainText_email)
    return header


'''
extract_body(plainText_email : str)
    extract the body part of the email
    return :
        - return the body (str)
'''
def extract_body(plainText_email):
    txt = re.findall("<body(.*\n*)*/html>", plainText_email)
    return txt


'''
extract_header(plainText_email : str)
    extract all the txt in the email
    return : 
        - return tab of all txt
'''
def extract_text(plainText_email):
    txt = re.findall("<p class=\"MsoNormal\">(.+?)<o:p>", plainText_email)
    return txt

# same as before but only return str
def extract_text_full(plainText_email):
    txt = re.findall("<p class=\"MsoNormal\">(.+?)<o:p>", plainText_email)
    tt = ''
    for i in txt:
        tt += i
    return tt

f = open("../email.txt", 'r')
print(extract_header(f.read()))
#print(extract_text_full(f.read()))
f.close()
import re


'''
extract_header(plainText_email : str)
    extract the header part of the email
    return : 
        - return the header (str)
'''
def extract_header(plainText_email):
    header = re.split("<body.*>", plainText_email)
    return header[0]


'''
extract_body(plainText_email : str)
    extract the body part of the email
    return :
        - return the body (str)
'''
def extract_body(plainText_email):
    txt = re.split("</head>", plainText_email)
    return txt[1]


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

"""
find_language(plainText_email : str)
    find the language
    return :
        - return the language
"""
def find_language(plainText_email):
    lang = re.findall('lang\=\"\w*\"', plainText_email)
    res = """"""
    inBracket = False

    for s in lang[0]:
        if s == '"' or s == "'":
            inBracket = not inBracket
            continue
        if inBracket :
            res += s

    return res


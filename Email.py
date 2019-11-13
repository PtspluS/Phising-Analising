import re

class Email:
    def __init__(self, email_brut = """"""):
        self.email_brut = email_brut
        self.header = """"""
        self.body = """"""
        self.lang = """"""
        self.text = """"""

        if re.search("<body>", email_brut) == None:
            self.type = 'plainText'
        else:
            self.type = 'html'

    '''
    extract_header()
        extract the header part of the email
        return : 
            - return the header (str)
    '''
    def extract_header(self):
        if self.type == 'html' :
            header = re.split("<body.*>", self.email_brut)
            return header[0]
        else :
            if re.search("Content-Transfer-Encoding:", self.email_brut) == None :
                header = re.split("Date : \.*\n", self.email_brut)
                header += re.findall("Date : \.*\n", self.email_brut)[0]
            else :
                header = re.split("Content-Transfer-Encoding: \.* \n", self.email_brut)

            return header[0]

    '''
    extract_body()
        extract the body part of the email
        return :
            - return the body (str)
    '''
    def extract_body(self):
        if self.type == 'html':
            txt = re.split("</head>", self.email_brut)
            return txt[1]
        else :
            if re.search("Content-Transfer-Encoding:", self.email_brut) == None :
                txt = re.split("Date : \.*\n", self.email_brut)
            else :
                txt = re.split("Content-Transfer-Encoding: \.* \n", self.email_brut)
            return txt[1]

    '''
    extract_header()
        extract all the txt in the email
        return : 
            - return tab of all txt
    '''
    def extract_txt(self):
        if self.type == 'html':
            txt = re.findall("<p class=\"MsoNormal\">(.+?)<o:p>", self.email_brut)
            return txt
        else :
            if re.search("Content-Transfer-Encoding:", self.email_brut) == None :
                txt = re.split("Date : \.*\n", self.email_brut)
            else :
                txt = re.split("Content-Transfer-Encoding: \.* \n", self.email_brut)
            return txt[1]

    # same as before but only return str
    def extract_text_full(self):
        if self.type == 'html':
            txt = re.findall("<p class=\"MsoNormal\">(.+?)<o:p>", self.email_brut)
            tt = ''
            for i in txt:
                tt += i
            return tt
        else :
            if re.search("Content-Transfer-Encoding:", self.email_brut) == None:
                txt = re.split("Date : \.*\n", self.email_brut)
            else:
                txt = re.split("Content-Transfer-Encoding: \.* \n", self.email_brut)
            return txt[1]

    """
    find_language()
        find the language
        return :
            - return the language
    """
    def find_language(self):
        if self.type == 'html':
            lang = re.findall('lang\=\"\w*\"', self.email_brut)
            res = """"""
            inBracket = False

            for s in lang[0]:
                if s == '"' or s == "'":
                    inBracket = not inBracket
                    continue
                if inBracket:
                    res += s

            return res

        else :
            return None


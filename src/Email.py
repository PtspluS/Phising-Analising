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

        self.header = self.extract_header(self.email_brut)
        self.body = self.extract_body(self.email_brut)
        self.text = self.extract_text_full(self.email_brut)
        self.lang = self.find_language()

    '''
    extract_header()
        extract the header part of the email
        return : 
            - return the header (str)
    '''
    def extract_header(self, txt):
        email_brut = (txt+'.')[:-1]
        if self.type == 'html' :
            header = re.split("<body.*>", email_brut)
            return header[0]
        else :
            if re.search("Content-Transfer-Encoding:", email_brut) == None :
                header = re.split("Date:.*\n", email_brut)
                #header += re.findall("Date:\.*\n", email_brut)[0]
            else :
                header = re.split("Content-Transfer-Encoding: .* \n", email_brut)

            return header[0]

    '''
    extract_body()
        extract the body part of the email
        return :
            - return the body (str)
    '''
    def extract_body(self, txt):
        email_brut = (txt + '.')[:-1]
        if self.type == 'html':
            txt = re.split("</head>", email_brut)
            return txt[1]
        else :
            if re.search("Content-Transfer-Encoding:", email_brut) == None :
                txt = re.split("Date:.*\n", email_brut)
            else :
                txt = re.split("Content-Transfer-Encoding: .* \n", email_brut)
            return txt[2]

    '''
    extract_header()
        extract all the txt in the email
        return : 
            - return tab of all txt
    '''
    def extract_txt(self, txt):
        email_brut = (txt + '.')[:-1]
        if self.type == 'html':
            txt = re.findall("<p class=\"MsoNormal\">(.+?)<o:p>", email_brut)
            return txt
        else :
            if re.search("Content-Transfer-Encoding:", email_brut) == None :
                txt = re.split("Date:.*\n", email_brut)
            else :
                txt = re.split("Content-Transfer-Encoding: .* \n", email_brut)
            return txt[2]

    # same as before but only return str
    def extract_text_full(self, txt):
        email_brut = (txt + '.')[:-1]
        if self.type == 'html':
            txt = re.findall("<p class=\"MsoNormal\">(.+?)<o:p>", email_brut)
            tt = """"""
            for i in txt:
                tt += i
            return tt
        else :
            if re.search("Content-Transfer-Encoding:", email_brut) == None:
                txt = re.split("Date:.*\n", email_brut)
            else:
                txt = re.split("Content-Transfer-Encoding: .* \n", email_brut)
            return txt[2]

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

    # get header
    def get_header(self):
        return self.header

    # get body
    def get_body(self):
        return self.body

    # get text
    def get_text(self):
        return self.text

    # get language
    def get_language(self):
        return self.lang

